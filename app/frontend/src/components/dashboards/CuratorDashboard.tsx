interface User {
    id: number;
    role: string;
    username: string;
}

const CuratorDashboard = ({ user }: { user: User }) => {
    return (
        <>
            <div>Curator: {user.id}</div>
        </>
    );
};

export { CuratorDashboard };
