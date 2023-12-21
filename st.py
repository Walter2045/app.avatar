import streamlit as st
st.title('Seu Personagem de Avatar')
st.subheader('Lenda de Aang')

opcao = st.selectbox('Qual o seu elemento favorito:',["Água","Terra",'Fogo',"Ar"])
if opcao == 'Água':
    imagem = 'agua.png'
    st.image(imagem, width=300)

    st.write('Elemento escolhido: ', opcao)

    radio_selecionado = st.radio('Selecione a variedade',["Gelo","Sangue"],horizontal=True)
    if radio_selecionado == 'Gelo':
    # Carregando e exibindo a imagem
        imagem = 'gelo.png'
        st.image(imagem, width=300)
    elif radio_selecionado == 'Sangue':
        imagem = 'sangue.png'
        st.image(imagem, width=300)

if opcao == 'Terra':
    imagem = 'terra.png'
    st.image(imagem, width=300)

    radio_selecionado = st.radio('Selecione a variedade',["Lama","Pedra"],horizontal=True)
    if radio_selecionado == 'Lama':
    # Carregando e exibindo a imagem
        imagem = 'lama.png'
        st.image(imagem, width=300)
    elif radio_selecionado == 'Pedra':
    # Carregando e exibindo a imagem
        imagem = 'pedra.png'
        st.image(imagem, width=300)


if opcao == 'Fogo':
    imagem = 'fogo.png'
    st.image(imagem, width=300)

    radio_selecionado = st.radio('Selecione a variedade',["Gas","Fogo Azul"],horizontal=True)
    if radio_selecionado == 'Gas':
    # Carregando e exibindo a imagem
        imagem = 'gas.png'
        st.image(imagem, width=300)
    elif radio_selecionado == 'Fogo Azul':
    # Carregando e exibindo a imagem
        imagem = 'azul.png'
        st.image(imagem, width=300)

if opcao == 'Ar':
    imagem = 'ar.png'
    st.image(imagem, width=300)

    radio_selecionado = st.radio('Selecione a variedade',["Balao","Lamina de Ar"],horizontal=True)
    if radio_selecionado == 'Balao':
    # Carregando e exibindo a imagem
        imagem = 'balao.png'
        st.image(imagem, width=300)
    elif radio_selecionado == 'Lamina de Ar':
    # Carregando e exibindo a imagem
        imagem = 'lamina.png'
        st.image(imagem, width=300)




# opcao1 = st.sidebar.checkbox('Opção 1')
# opcao2 = st.sidebar.selectbox('Opção 1',['1','2','3','4',])

# opcao2 = st.sidebar.slider('Opção 1',0,1,10)

