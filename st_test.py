import streamlit as st
import numpy as np
import matplotlib.pylab as plt

st.set_page_config(layout="wide")

left, right = st.columns(2)

with left:
    st.title('This is for Title')
    st.text('This is for Text')
    st.caption('This is for caption')
    st.header('This is for Header')
    st.subheader('This is for subhead')
    st.write('This is for writing')

    st.code(
        """
        a = int(input())
        b = int(input())
        if (a>b):
           print(a)
        else:
           print(b)
        """
    )

    st.latex('\int f^{-1}(x-x_a)\,dx')

    choose = st.radio("Select a option",('Bengali', 'Marathi', 'Hindi'))

    if choose == 'Bengali':
        st.text('West Bengal')
    elif choose == 'Marathi':
        st.text('Maharashtra')
    if choose == 'Hindi':
        st.text('Delhi')

with right:
    st.title("Simulation[tm]")
    st.write("Here is our super important simulation")

    st.sidebar.markdown("## Controls")
    st.sidebar.markdown("You can **change** the values to change the *chart*.")
    x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
    y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

    st.write(f"x={x} y={y}")
    values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)

    for i in range(values.shape[1]):
        plt.plot(values[:, i])

    st.pyplot()

    """def plot_metrics(metrics_list):
            if "Confusion Matrix" in metrics_list:
                st.subheader("Confusion Matrix")
                plot_confusion_matrix(model, x_test, y_test, display_labels=class_names)
                st.pyplot()
            if "ROC Curve" in metrics_list:
                st.subheader("ROC Curve")
                plot_roc_curve(model, x_test, y_test)
                st.pyplot()
            if "Precision-Recall Curve" in metrics_list:
                st.subheader("Precision-Recall Curve")
                plot_precision_recall_curve(model, x_test, y_test)
                st.pyplot()"""