import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '../Button';
import { makeApiRequest } from '../../utils/requests';
import { FileUpIcon } from 'lucide-react';

interface User {
    id: number;
    role: string;
    username: string;
}

interface Document {
    id: number;
    title: string;
    type: string;
    source: string;
    added_by: number;
    has_been_processed: boolean;
    timestamp: string | null;
}

const CuratorDashboard = ({ user }: { user: User }) => {
    const [documents, setDocuments] = useState<Document[]>([]);
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const navigate = useNavigate();

    const fetchDocuments = useCallback(async () => {
        try {
            const response = await makeApiRequest(
                'curator/get_documents',
                'GET'
            );
            console.log('Document retrieval successful:', response);
            setDocuments(response.documents);
        } catch (error) {
            console.log('Error while retrieving documents:', error);
        }
    }, []);

    useEffect(() => {
        fetchDocuments();
    }, [fetchDocuments]);

    const handleUploadFile = async (file: File) => {
        if (!file) {
            return;
        }

        try {
            // convert file to base64 for uploading
            const fileDataBase64 = await new Promise<string>(
                (resolve, reject) => {
                    const reader = new FileReader();
                    reader.onload = () => {
                        const result = reader.result;
                        if (typeof result === 'string') {
                            resolve(result.split(',')[1]);
                        } else {
                            reject(new Error('Failed to read file as string.'));
                        }
                    };
                    reader.onerror = () =>
                        reject(new Error('File reading failed.'));
                    reader.readAsDataURL(file);
                }
            );

            const mediaType = file.type;

            const documentData = {
                filename: file.name,
                media_type: mediaType,
                file_data: fileDataBase64,
                added_by: user.id,
            };

            const response = await makeApiRequest(
                'curator/upload_document',
                'POST',
                documentData
            );
            await fetchDocuments();
            setSelectedFile(null);
            console.log('File upload successful', response);
        } catch (error) {
            console.log('Error while uploading document:', error);
        }
    };

    const handleRemoveFile = async (document_id: number) => {
        try {
            const response = await makeApiRequest(
                `curator/delete_document/${document_id}`,
                'DELETE'
            );
            await fetchDocuments();
            console.log('Document deletion successful:', response);
        } catch (error) {
            console.log('Error while deleting document:', error);
        }
    };

    return (
        <>
            <div className="flex flex-col h-screen items-center justify-center gap-8">
                <div className="fixed top-4 left-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 text-xl px-4 py-2 rounded-xs">
                    <div className="flex flex-col gap-2">
                        <div>
                            <span className="font-bold underline decoration-2">
                                Username:
                            </span>{' '}
                            {user.username}
                        </div>
                        <div>
                            <span className="font-bold underline decoration-2">
                                Role:
                            </span>{' '}
                            {user.role}
                        </div>
                        <div>
                            <span className="font-bold underline decoration-2">
                                ID:
                            </span>{' '}
                            {user.id}
                        </div>
                        <Button
                            onClick={() =>
                                navigate('/', { replace: true, state: {} })
                            }
                            variant="destructive"
                            size="small"
                        >
                            Log Out
                        </Button>
                    </div>
                </div>

                <div className="flex flex-col items-center gap-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 p-4 rounded-xs">
                    <div className="flex flex-row items-center w-full">
                        <h1 className="text-3xl underline decoration-2">
                            All Documents
                        </h1>
                        <div className="flex grow"></div>
                        <div className="flex flex-col bg-green-800 text-green-200 rounded-xs">
                            <input
                                type="file"
                                id="file-upload"
                                onChange={(e) => {
                                    const file = e.target.files?.[0];
                                    if (file) {
                                        setSelectedFile(file);
                                        handleUploadFile(file);
                                    }
                                }}
                                className="hidden"
                            />
                            <label
                                htmlFor="file-upload"
                                className="flex flex-row gap-2 px-2 py-2 font-semibold hover:cursor-pointer"
                            >
                                <FileUpIcon />
                                {selectedFile
                                    ? selectedFile.name
                                    : 'Upload Document'}
                            </label>
                        </div>
                    </div>

                    <div className="overflow-x-auto rounded-xs">
                        <table className="w-full border-collapse">
                            <thead>
                                <tr className="bg-neutral-700">
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        ID
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Title
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Type
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Source
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Added By
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Previously Processed
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Timestamp
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {documents.map((document) => (
                                    <tr
                                        key={document.id}
                                        className="hover:bg-neutral-800"
                                    >
                                        <td className="border-2 bg-neutral-800 hover:bg-neutral-700 border-neutral-600 px-4 py-2 text-center">
                                            {document.id}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.title}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.type}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.source}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.added_by}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.has_been_processed
                                                ? 'Yes'
                                                : 'No'}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {document.timestamp
                                                ? new Date(
                                                      document.timestamp
                                                  ).toLocaleString('en-US', {
                                                      timeZone:
                                                          'America/Chicago',
                                                  })
                                                : 'N/A'}
                                        </td>
                                        <td className="px-4 py-2 bg-neutral-900 hover:bg-neutral-900">
                                            <Button
                                                onClick={() => {
                                                    handleRemoveFile(
                                                        document.id
                                                    );
                                                }}
                                                variant="destructive"
                                                size="small"
                                            >
                                                Delete
                                            </Button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </>
    );
};

export { CuratorDashboard };
