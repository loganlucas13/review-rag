import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '../Button';
import { Input } from '../Input';
import { makeApiRequest } from '../../utils/requests';

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

const EndUserDashboard = ({ user }: { user: User }) => {
    const [query, setQuery] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [output, setOutput] = useState('');
    const [documents, setDocuments] = useState<Document[]>([]);
    const [currentDocument, setCurrentDocument] = useState(-1);
    const navigate = useNavigate();

    const handleQuerySubmit = async (query: string, document_id: number) => {
        const queryDetails = {
            query: query,
            user_id: user.id,
            document_id: document_id,
        };
        try {
            const response = await makeApiRequest(
                'enduser/submit_query',
                'POST',
                queryDetails
            );
            setOutput(response.results.cosine_similarity[0].text);
            console.log('Query submitted successfully:', response);
        } catch (error) {
            console.log('Error while submitting query:', error);
            setOutput('Error while submitting query...');
        }
    };

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

    return (
        <>
            <div className="flex flex-col h-screen items-center justify-center gap-4">
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

                <div className="flex flex-col items-center gap-2 pb-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 p-4 rounded-xs">
                    <h1 className="text-2xl font-semibold underline decoration-2 pb-2">
                        Available Documents
                    </h1>
                    {documents && documents.length > 0 ? (
                        documents.map((document) => (
                            <Button
                                key={document.id}
                                className={
                                    `border-2 px-2 py-1 rounded-xs hover:cursor-pointer w-full ` +
                                    (currentDocument === document.id
                                        ? 'bg-neutral-600 text-neutral-300 border-neutral-300'
                                        : 'border-neutral-500 text-neutral-300')
                                }
                                onClick={() => {
                                    setCurrentDocument(document.id);
                                }}
                                variant="none"
                            >
                                {document.title}
                            </Button>
                        ))
                    ) : (
                        <span>No documents found.</span>
                    )}
                </div>

                <div className="flex flex-col w-1/2 items-center gap-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 p-4 rounded-xs">
                    {submitted && (
                        <div className="w-full h-fit bg-neutral-800 border-2 border-neutral-600 rounded-xs p-4 overflow-y-auto">
                            {output || ''}
                        </div>
                    )}

                    <div className="flex flex-row gap-2 w-full">
                        <Input
                            value={query}
                            onChange={setQuery}
                            placeholder="Make a query..."
                            className="w-full"
                        />
                        <Button
                            onClick={() => {
                                setSubmitted(true);
                                handleQuerySubmit(query, currentDocument);
                            }}
                            variant="approval"
                        >
                            Submit
                        </Button>
                    </div>
                </div>
            </div>
        </>
    );
};

export { EndUserDashboard };
