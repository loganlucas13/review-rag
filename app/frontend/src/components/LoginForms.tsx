import { useState } from 'react';
import { clamp } from '../utils/clamp';
import { ArrowBigLeftDashIcon } from 'lucide-react';

type FormProps = {
    goBack: () => void;
};

const HomeButton = ({ goBack }: FormProps) => {
    return (
        <button
            onClick={() => goBack()}
            className="flex bg-slate-900 text-slate-400 border-2 border-slate-600 p-3 rounded-xs hover:cursor-pointer"
        >
            <ArrowBigLeftDashIcon size={32} />
        </button>
    );
};

const LoginForm = ({ goBack }: FormProps) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = () => {
        // TODO: make request to backend Flask API to log in user with current credentials
        return;
    };

    return (
        <>
            <HomeButton goBack={goBack} />
            <div className="flex flex-col items-center justify-center gap-4 bg-slate-900 text-slate-400 border-2 border-slate-600 px-2 py-2 rounded-xs w-1/5 mr-[60px]">
                <h1 className="text-2xl font-semibold">Log In</h1>
                <div className="flex flex-col gap-2 w-full">
                    <input
                        placeholder="Username"
                        className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                        onChange={(e) => setUsername(e.target.value)}
                        value={username}
                    ></input>
                    <input
                        placeholder="Password"
                        type="password"
                        className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                    ></input>

                    <button
                        onClick={() => {
                            handleSubmit();
                        }}
                        className="bg-slate-600 text-slate-400 text-lg font-semibold rounded-xs hover:cursor-pointer"
                    >
                        Submit
                    </button>
                </div>
            </div>
        </>
    );
};

const SignupForm = ({ goBack }: FormProps) => {
    // all required user credentials
    const [role, setRole] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    const availableRoles = ['Admin', 'Curator', 'End User'];
    const handleRoleClick = (selectedRole: string) => {
        setRole(selectedRole);
        return;
    };

    // handling next/back buttons
    const [currentTab, setCurrentTab] = useState(0);
    const handleTabSwitch = (direction: string) => {
        let newTab;
        if (direction === 'forward') {
            if (!role || !username || !password) {
                return; // TODO: add error popup
            }
            newTab = currentTab + 1;
        } else {
            newTab = currentTab - 1;
        }
        setCurrentTab(clamp(newTab, 0, 1));
    };

    const handleSubmit = () => {
        // TODO: make request to backend to create user in database
        if (!role || !username || !password || !name || !email) {
            return; // TODO: add error popup
        }
    };

    return (
        <>
            <HomeButton goBack={goBack} />
            <div className="flex flex-col items-center justify-center gap-4 bg-slate-900 text-slate-400 border-2 border-slate-600 px-2 py-2 rounded-xs w-1/5 mr-[60px]">
                <h1 className="text-2xl font-semibold">Sign Up</h1>
                <div className="flex flex-col gap-2 w-full">
                    {/* role options */}
                    {currentTab === 0 && (
                        <div className="flex flex-row gap-2 pb-4">
                            {availableRoles.map((role_type) => (
                                <button
                                    key={role_type}
                                    className={
                                        `border-2 px-1 py-1 w-1/3 rounded-xs hover:cursor-pointer ` +
                                        (role_type === role
                                            ? 'bg-slate-600 text-slate-400'
                                            : 'border-slate-500')
                                    }
                                    onClick={() => {
                                        handleRoleClick(role_type);
                                    }}
                                >
                                    {role_type}
                                </button>
                            ))}
                        </div>
                    )}

                    {/* input boxes */}
                    {currentTab === 0 && (
                        <>
                            <input
                                placeholder="Username"
                                className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                                onChange={(e) => setUsername(e.target.value)}
                                value={username}
                            ></input>
                            <input
                                placeholder="Password"
                                type="password"
                                className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                                onChange={(e) => setPassword(e.target.value)}
                                value={password}
                            ></input>
                        </>
                    )}
                    {currentTab === 1 && (
                        <>
                            <input
                                placeholder="Name"
                                className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                                onChange={(e) => setName(e.target.value)}
                                value={name}
                            ></input>
                            <input
                                placeholder="Email"
                                type="password"
                                className="border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs"
                                onChange={(e) => setEmail(e.target.value)}
                                value={email}
                            ></input>
                        </>
                    )}

                    {/* confirm buttons at bottom */}
                    {currentTab === 0 && (
                        <>
                            <button
                                onClick={() => {
                                    handleTabSwitch('forward');
                                }}
                                className="bg-slate-600 text-slate-400 text-lg font-semibold rounded-xs hover:cursor-pointer"
                            >
                                Next
                            </button>
                        </>
                    )}
                    {currentTab === 1 && (
                        <>
                            <div className="flex flex-row gap-2 w-full">
                                <button
                                    onClick={() => {
                                        handleTabSwitch('back');
                                    }}
                                    className="bg-red-400 text-red-900 text-lg font-semibold rounded-xs hover:cursor-pointer px-2"
                                >
                                    Back
                                </button>
                                <button
                                    onClick={() => {
                                        handleSubmit();
                                    }}
                                    className="w-full bg-slate-600 text-slate-400 text-lg font-semibold rounded-xs hover:cursor-pointer"
                                >
                                    Submit
                                </button>
                            </div>
                        </>
                    )}
                </div>
            </div>
        </>
    );
};

export { LoginForm, SignupForm };
