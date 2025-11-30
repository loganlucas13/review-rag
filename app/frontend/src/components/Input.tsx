type InputProps = {
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
    type?: string;
    className?: string;
};

const Input = ({
    value,
    onChange,
    placeholder,
    type,
    className,
}: InputProps) => {
    return (
        <input
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            type={type}
            className={`border-2 px-2 py-1 border-neutral-500 focus:outline-none focus:border-neutral-200 rounded-xs ${className}`}
        />
    );
};

export { Input };
