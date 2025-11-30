import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '../Button';
import { Input } from '../Input';
import { makeApiRequest } from '../../utils/requests';

interface User {
    id: number;
    role: string;
    username: string;
}

const EndUserDashboard = ({ user }: { user: User }) => {
    const [query, setQuery] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [output, setOutput] = useState('');
    const navigate = useNavigate();

    return (
        <>
            <div className="flex flex-col h-screen items-center justify-center gap-16">
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

                <div className="flex flex-col w-1/2 items-center gap-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 p-4 rounded-xs">
                    {submitted && (
                        <div className="w-full h-fit bg-neutral-800 border-2 border-neutral-600 rounded-xs p-4 overflow-y-auto">
                            {output || 'TODO'}
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
                            onClick={() => setSubmitted(true)}
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
