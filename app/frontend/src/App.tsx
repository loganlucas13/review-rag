import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Background from './components/Background';
import LoginPage from './pages/LoginPage';

const App = () => {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route element={<Background />}>
                        <Route path="/" element={<LoginPage />}></Route>
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    );
};

export default App;
