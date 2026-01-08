import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("最初の第一歩")

import streamlit as st

st.title("今日の気分・状態アプリ")

st.write("今の自分の気分を選んでみてください。")

if st.button("😀 元気"):
    st.write("今日は元気です！いろいろ挑戦したい気分です。")

if st.button("😐 普通"):
    st.write("特に変わりはない、いつも通りの一日です。")

if st.button("😴 眠い"):
    st.write("少し疲れているので、ゆっくり過ごしたいです。")

if st.button("😣 疲れた"):
    st.write("今日は少し疲れています。早めに休みたいです。")
