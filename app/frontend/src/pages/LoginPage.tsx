import { useState } from 'react';
import { LoginForm, SignupForm } from '../components/LoginForms';
import { Button } from '../components/Button';

const LoginPage = () => {
    const [currentForm, setCurrentForm] = useState('');

    return (
        <>
            <div className="h-screen flex flex-row gap-4 items-center justify-center">
                {currentForm === '' && (
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
