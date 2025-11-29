import { Outlet } from 'react-router-dom';
import Dither from './Dither';

const Background = () => {
    return (
        <div className="w-screen h-screen relative overflow-hidden bg-black">
            <div className="absolute inset-0 z-0">
                <Dither
                    waveSpeed={0.005}
                    waveFrequency={2}
                    waveColor={[0.5, 0.5, 0.5]}
                    colorNum={8}
                />
            </div>
            <div className="relative z-10 w-full h-full overflow-auto">
                <Outlet />
            </div>
        </div>
    );
};

export default Background;
