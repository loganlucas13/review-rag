import axios, { type AxiosRequestConfig } from 'axios';

const makeApiRequest = async (
    endpoint: string,
    method: string = 'GET',
    data?: unknown,
    config?: AxiosRequestConfig
) => {
    const apiUrl = 'http://localhost:4196/api/';

    try {
        const response = await axios({
            method,
            url: `${apiUrl}${endpoint}`,
            data,
            headers: {
                'Content-Type': 'application/json',
            },
            ...config,
        });

        return response.data;
    } catch (error) {
        console.log(error);
        throw error;
    }
};

export { makeApiRequest };
