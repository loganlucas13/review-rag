type ButtonVariants = 'primary' | 'secondary' | 'destructive';
type ButtonSize = 'default' | 'small' | 'large';

const variantStyles = {
    primary:
        'bg-slate-900 text-slate-400 border-2 border-slate-600 font-semibold',
    secondary: 'bg-slate-600 text-slate-400 text-lg font-semibold',
    destructive: 'bg-red-400 text-red-900',
};

const sizeStyles = {
    default: 'px-4 py-2',
    small: 'px-2',
    large: 'px-4 py-2 text-3xl',
};

type ButtonProps = {
    onClick: () => void;
    children: React.ReactNode;
    variant?: ButtonVariants;
    size?: ButtonSize;
    className?: string;
};

const Button = ({
    onClick,
    children,
    variant = 'primary',
    size = 'default',
    className = '',
}: ButtonProps) => {
    const defaultStyles = 'rounded-xs hover: cursor-pointer';
    const combinedClasses =
        `${defaultStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${className}`.trim();

    return (
        <button onClick={onClick} className={combinedClasses}>
            {children}
        </button>
    );
};

export { Button };
