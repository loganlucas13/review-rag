import { useLocation, useNavigate } from 'react-router-dom';
import { AdminDashboard } from '../components/dashboards/AdminDashboard';
import { CuratorDashboard } from '../components/dashboards/CuratorDashboard';
import { EndUserDashboard } from '../components/dashboards/EndUserDashboard';
import { Button } from '../components/Button';

interface User {
    id: number;
    role: string;
    username: string;
}

const DashboardPage = () => {
    const location = useLocation();
    const { user } = location.state as { user: User };
    const navigate = useNavigate();

    if (!user) {
        <div className="flex h-screen items-center justify-center">
            <div className="flex flex-col gap-4 p-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 justify-center items-center rounded-xs">
                <span>ERROR: No user logged in (no user).</span>
                <Button
                    onClick={() => {
                        navigate('/');
                    }}
                    variant="destructive"
                >
                    Go Back
                </Button>
            </div>
        </div>;
    }

    switch (user.role) {
        case 'Admin':
            return <AdminDashboard user={user} />;
        case 'Curator':
            return <CuratorDashboard user={user} />;
        case 'EndUser':
            return <EndUserDashboard user={user} />;
        default:
            return (
                <div className="flex h-screen items-center justify-center">
                    <div className="flex flex-col gap-4 p-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 justify-center items-center rounded-xs">
                        <span>ERROR: No user logged in (invalid role).</span>
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
