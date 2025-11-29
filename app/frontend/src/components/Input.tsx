type InputProps = {
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
    type?: string;
};

const Input = ({ value, onChange, placeholder, type }: InputProps) => {
    return (
        <input
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            type={type}
            className={`border-2 px-2 py-1 border-slate-500 focus:outline-none rounded-xs`}
        />
    );
};

export { Input };
