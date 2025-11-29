import { useState } from 'react';
import { LoginForm, SignupForm } from '../components/LoginForms';
import { Button } from '../components/Button';

const LoginPage = () => {
    const [currentForm, setCurrentForm] = useState('');

    return (
        <>
            <div className="h-screen flex flex-row gap-4 items-center justify-center">
                {currentForm === '' && (
                    <div className="flex flex-col gap-8 px-4 py-2 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 rounded-xs">
                        <span className="text-4xl font-bold px-4 pt-4">
                            Document Q&A
                        </span>
                        <div className="flex flex-col gap-4">
                            <Button
                                onClick={() => setCurrentForm('log in')}
                                size="large"
                            >
                                Log In
                            </Button>

                            <Button
                                onClick={() => setCurrentForm('sign up')}
                                size="large"
                            >
                                Sign Up
                            </Button>
                        </div>
                    </div>
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
