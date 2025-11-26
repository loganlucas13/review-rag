import { useState } from 'react';
import { LoginForm, SignupForm } from '../components/LoginForms';

const LoginPage = () => {
    const [currentForm, setCurrentForm] = useState('');

    return (
        <>
            <div className="h-screen flex flex-row gap-4 items-center justify-center">
                {currentForm === '' && (
                    <>
                        <div className="flex flex-col gap-4">
                            <button
                                onClick={() => {
                                    setCurrentForm('log in');
                                }}
                                className="px-4 py-2 bg-slate-900 text-slate-400 border-2 border-slate-600 text-2xl font-semibold rounded-xs hover:cursor-pointer"
                            >
                                Log In
                            </button>

                            <button
                                onClick={() => {
                                    setCurrentForm('sign up');
                                }}
                                className="px-4 py-2 bg-slate-900 text-slate-400 border-2 border-slate-600 text-2xl font-semibold rounded-xs hover:cursor-pointer"
                            >
                                Sign Up
                            </button>
                        </div>
                    </>
                )}

                {currentForm === 'log in' && (
                    <LoginForm goBack={() => setCurrentForm('')} />
                )}
                {currentForm === 'sign up' && (
                    <SignupForm goBack={() => setCurrentForm('')} />
                )}
            </div>
        </>
    );
};

export default LoginPage;
