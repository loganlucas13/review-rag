interface User {
    id: number;
    role: string;
    username: string;
}

const EndUserDashboard = ({ user }: { user: User }) => {
    return (
        <>
            <div>End User: {user.id}</div>
        </>
    );
};

export { EndUserDashboard };
