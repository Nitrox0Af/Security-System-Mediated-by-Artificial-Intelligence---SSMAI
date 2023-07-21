# PICII

## Introdução:
Com o objetivo de produzir um trabalho que integra software e hardware para a matéria de Projeto Integrado de Computação II (PIC II), os alunos da graduação do curso de Engenharia de Computação da Universidade Federal do Espírito Santo, Gabrielly Cariman e Mayke Wallace, desenvolveram um projeto voltado para a área de segurança. A ideia era construir um sistema domiciliar baseado em reconhecimento facial utilizando inteligência artificial, e, devido a isso, o grupo foi nomeado como "Security System Mediated by Artificial Intelligence" (SSMAI). O trabalho foi dividido em tarefas (tasks), que tinham uma label em comum, sendo de hardware ou de software, que foram comumente divididas pela equipe. A explicação do produto final encontra-se abaixo:
[![SSMAI](img/photo_2023-07-21_09-23-27.jpg)](https://www.youtube.com/watch?v=Hd1foBAOOVI&t=1s)

## Como usar:
### **Software**:

### **hardware**:
#### Lista de materiais:
    - 01 Piezo Buzzer;
    - 01 LED vermelho;
    - 01 LED verde;
    - Reistores:
        - 2 330 Ω; 
        - 4 1 kΩ; 
        - 1 10 kΩ;
    - 01 raspberry pi 3 b+ ( **Raspberry OS 64-bit** )
    - 01 TIP42C
    - 01 TIP31C
    - Jumpers
    - 01 reed switch
    - 01 ímâ
    - 01 maquete de porta eletronica
    - 01 camera
    - 01 ultrassom
 
#### Funcionamento:
O sistema é bem simples. O sensor Reed Switch monitora se a porta está fechada ou aberta. Caso a porta esteja aberta, as opções de entrar com o reconhecimento facial ou com a sequência de dígitos ficam bloqueadas até a porta voltar ao estado de fechada, pois não faria sentido tentar abrir uma porta que já está aberta. Com a porta fechada, existem duas formas de poder abri-la, como mencionado anteriormente: com reconhecimento facial ou sequência de senha.

Por padrão, as senhas são de 4 dígitos e são "1234". Entretanto, existe uma terceira opção para trocar essa senha, nesse caso, o sistema irá pedir para entrar com uma senha de 8 dígitos para poder trocar a senha de 4 dígitos, "12345678".

Em caso de erro na digitação da senha correta, o sistema notificará que a senha colocada está errada, o LED vermelho piscará 3 vezes e um buzzer emitirá um som de apito por 1 segundo.

A opção de abrir a porta por reconhecimento facial é uma segunda alternativa. Ao ser selecionada, o sistema fica monitorando a distância que um rosto de uma pessoa está em relação à câmera. Ao chegar a menos de 40 cm da câmera e após 3 segundos, a câmera tirará uma foto da pessoa presente. Após a confirmação, o sistema fará o match do rosto da pessoa com os rostos presentes no banco de dados do site. Ao obter um resultado, uma mensagem será enviada para o Telegram cadastrado. Pelo Telegram, o dono do produto receberá a foto de quem está querendo abrir a porta e poderá selecionar duas opções: abrir a porta ou mantê-la fechada.