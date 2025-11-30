import { useState, useEffect } from 'react';
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

    const fetchDocuments = async () => {
        // TODO: get all documents from database + update state
        return;
    };

    // TODO: get documents from api on mount and update state
    useEffect(() => {}, []);

    const handleUploadFile = async () => {
        // TODO: upload file to database (use makeApiRequest)
        return;
    };

    const handleRemoveFile = async () => {
        // TODO: remove file from database (use makeApiRequest)
        return;
    };

    return (
        <>
            <div className="flex flex-col h-screen items-center justify-center gap-8">
                <div className="fixed top-4 left-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 text-2xl px-4 py-2 rounded-xs">
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
                                onChange={(e) =>
                                    setSelectedFile(e.target.files[0])
                                }
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
                                        Last Activity
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
                                            {document.has_been_processed}
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
                                                onClick={() => {}}
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
