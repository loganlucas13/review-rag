import { useLocation, useNavigate } from 'react-router-dom';
import { AdminDashboard } from '../components/dashboards/AdminDashboard';
import { CuratorDashboard } from '../components/dashboards/CuratorDashboard';
import { EndUserDashboard } from '../components/dashboards/EndUserDashboard';
import { Button } from '../components/Button';

type UserRole = 'admin' | 'curator' | 'end user' | null;

interface User {
    name: string;
    email: string;
    role: UserRole;
    username: string;
}

const DashboardPage = () => {
    const location = useLocation();
    const { user } = location.state as { user: User };
    const navigate = useNavigate();

    // NOTE: TESTING
    // const user: User = {
    //     name: 'name',
    //     email: 'email',
    //     role: null,
    //     username: 'username',
    // };

    if (!user) {
        return <div>ERROR: No user logged in.</div>;
    }

    switch (user.role) {
        case 'admin':
            return <AdminDashboard user={user} />;
        case 'curator':
            return <CuratorDashboard user={user} />;
        case 'end user':
            return <EndUserDashboard user={user} />;
        default:
            return (
                <div className="flex h-screen items-center justify-center">
                    <div className="flex flex-col gap-4 p-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 justify-center items-center rounded-xs">
                        <span>ERROR: No user logged in.</span>
                        <Button
                            onClick={() => {
                                navigate('/');
                            }}
                            variant="destructive"
                        >
                            Go Back
                        </Button>
                    </div>
                </div>
            );
    }
};

export default DashboardPage;
