import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Background from './components/Background';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';

const App = () => {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route element={<Background />}>
                        <Route path="/" element={<LoginPage />} />
                        <Route path="/dashboard" element={<DashboardPage />} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    );
};

export default App;
