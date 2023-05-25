import React, { useRef } from 'react';
import axios from 'axios';

const Inputs = () => {
  const csrfTokenRef = useRef<HTMLInputElement>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const csrfToken = csrfTokenRef.current?.value;

    try {
      const response = await axios.post('http://localhost:8000/api/receber-strings/', String, {
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Token ${csrfToken}'
        },
      });

      if (response.status === 200) {
        console.log('enviado');
      } else {
        console.error('Erro ao enviar as strings.');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="hidden" name="csrfmiddlewaretoken" ref={csrfTokenRef} />
  
      <input type="text" name="str_1" />
      <input type="text" name="str_2" />
      <input type="text" name="str_3" />
      <input type="text" name="str_4" />
      <input type="text" name="str_5" />
  
      <button type="submit">Enviar</button>
    </form>
  );
};

export default Inputs;