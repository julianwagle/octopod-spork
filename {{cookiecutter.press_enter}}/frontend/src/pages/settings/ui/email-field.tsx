import { useField } from 'effector-forms';
import { InputField } from 'ui';
import { form } from '../model';

export const EmailField: React.FC = () => {
  const { value, name, onChange } = useField(form.fields.email);

  return (
    <InputField
      className="form-control-lg"
      name={name}
      placeholder="Email"
      type="email"
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
};
