import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { makeApiRequest } from '../../utils/requests';
import { Button } from '../Button';
import { Input } from '../Input';

interface User {
    id: number;
    role: string;
    username: string;
}

interface RegisteredUser {
    id: number;
    role: string;
    username: string;
    password: string;
    email: string;
    name: string;
    last_activity_timestamp: string | null;
}

const AdminDashboard = ({ user }: { user: User }) => {
    const [registeredUsers, setRegisteredUsers] = useState<RegisteredUser[]>(
        []
    );
    const [userToEdit, setUserToEdit] = useState(-1);
    const [newRole, setNewRole] = useState('');
    const [newUsername, setNewUsername] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [newEmail, setNewEmail] = useState('');
    const [newName, setNewName] = useState('');

    const navigate = useNavigate();

    const availableRoles = ['Admin', 'Curator', 'EndUser'];

    const fetchUsers = useCallback(async () => {
        try {
            const response = await makeApiRequest(
                'admin/retrieve_registered_users',
                'GET'
            );
            console.log('User retrieval successful:', response);
            setRegisteredUsers(response.users);
        } catch (error) {
            console.log('Error while retrieving users:', error);
        }
    }, []);

    useEffect(() => {
        fetchUsers();
    }, [fetchUsers]);

    const handleUpdateClick = () => {
        const updateUser = async () => {
            const userData = {
                role: newRole,
                username: newUsername,
                password: newPassword,
                name: newName,
                email: newEmail,
            };
            try {
                const response = await makeApiRequest(
                    `admin/edit_profile/${userToEdit}`,
                    'PUT',
                    userData
                );
                setUserToEdit(-1);
                await fetchUsers();
                console.log('Profile update successful:', response);
            } catch (error) {
                console.log('Error while updating profile:', error);
            }
        };
        updateUser();
    };

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

                <div className="flex flex-col items-center gap-4 bg-neutral-900 text-neutral-300 border-2 border-neutral-600 p-4 rounded-xs">
                    <h1 className="text-3xl underline decoration-2">
                        All Users
                    </h1>
                    <div className="overflow-x-auto rounded-xs">
                        <table className="w-full border-collapse">
                            <thead>
                                <tr className="bg-neutral-700">
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        ID
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Role
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Username
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Password
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Email
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Name
                                    </th>
                                    <th className="border-2 border-neutral-600 px-4 py-2 text-center">
                                        Last Activity
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {registeredUsers.map((registeredUser) => (
                                    <tr
                                        key={registeredUser.id}
                                        className="hover:bg-neutral-800"
                                    >
                                        <td className="border-2 bg-neutral-800 hover:bg-neutral-700 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.id}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.role}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.username}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.password}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.email}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.name}
                                        </td>
                                        <td className="border-2 border-neutral-600 px-4 py-2 text-center">
                                            {registeredUser.last_activity_timestamp
                                                ? new Date(
                                                      registeredUser.last_activity_timestamp
                                                  ).toLocaleString('en-US', {
                                                      timeZone:
                                                          'America/Chicago',
                                                  })
                                                : 'N/A'}
                                        </td>
                                        <td className="px-4 py-2 bg-neutral-900 hover:bg-neutral-900">
                                            <Button
                                                onClick={() => {
                                                    setUserToEdit(
                                                        registeredUser.id
                                                    );
                                                }}
                                                variant="destructive"
                                                size="small"
                                            >
                                                Edit
                                            </Button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    {userToEdit != -1 && (
                        <div className="flex flex-col border-2 border-neutral-600 w-full p-4 items-center justify-center gap-4">
                            <span className="text-xl underline decoration-2 text-center">
                                Editing User ID {userToEdit}
                            </span>
                            <div className="flex flex-col gap-2">
                                <div className="flex flex-row gap-2 pb-4 justify-center">
                                    {availableRoles.map((role_type) => (
                                        <button
                                            key={role_type}
                                            className={
                                                `border-2 px-1 py-1 w-1/4 rounded-xs hover:cursor-pointer ` +
                                                (role_type === newRole
                                                    ? 'bg-neutral-600 text-neutral-300'
                                                    : 'border-neutral-500')
                                            }
                                            onClick={() => {
                                                setNewRole(role_type);
                                            }}
                                        >
                                            {role_type}
                                        </button>
                                    ))}
                                </div>
                                <div className="flex flex-row gap-6">
                                    <Input
                                        onChange={setNewUsername}
                                        value={newUsername}
                                        placeholder="New Username"
                                    />
                                    <Input
                                        onChange={setNewPassword}
                                        value={newPassword}
                                        placeholder="New Password"
                                        type="password"
                                    />
                                    <Input
                                        onChange={setNewEmail}
                                        value={newEmail}
                                        placeholder="New Email"
                                    />
                                    <Input
                                        onChange={setNewName}
                                        value={newName}
                                        placeholder="New Name"
                                    />
                                </div>
                            </div>
                            <Button
                                onClick={handleUpdateClick}
                                variant="destructive"
                                className="w-full font-semibold"
                            >
                                Update User
                            </Button>
                        </div>
                    )}
                </div>
            </div>
        </>
    );
};

export { AdminDashboard };
