type UserRole = 'admin' | 'curator' | 'end user' | null;

interface User {
    name: string;
    email: string;
    role: UserRole;
    username: string;
}

const AdminDashboard = ({ user }: { user: User }) => {
    return (
        <>
            <div>{user.name}</div>
        </>
    );
};

export { AdminDashboard };
