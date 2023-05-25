import React, { useState, ChangeEvent, FormEvent } from 'react';

function App(): JSX.Element {
  const [var1, setVar1] = useState('');
  const [var2, setVar2] = useState('');
  const [resultado, setResultado] = useState('');

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>, setValue: React.Dispatch<React.SetStateAction<string>>): void => {
    const { value } = event.target;
    setValue(value);
  };

  const handleFormSubmit = async (event: FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    const response = await fetch('http://localhost:8000/api/soma/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ var_1: var1, var_2: var2 }),
    });

    const data = await response.json();
    setResultado(data.resultado);
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <label>
          Variável 1:
          <input
            type="number"
            value={var1}
            onChange={(event) => handleInputChange(event, setVar1)}
          />
        </label>
        <br />
        <label>
        Variável 2:
        <input
          type="number"
          value={var2}
          onChange={(event) => handleInputChange(event, setVar2)}
        />
      </label>
      <br />
      <button type="submit">Enviar</button>
    </form>
    <br />
    {resultado && <p>Resultado: {resultado}</p>}
  </div>
);
}

export default App;