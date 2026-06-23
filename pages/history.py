import streamlit as st
import pandas as pd

st.title("📜 Translation History")

history_file = "data/translation_history.csv"

try:
    df = pd.read_csv(history_file)

    st.dataframe(
        df,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="⬇ Download History",
            data=df.to_csv(index=False),
            file_name="translation_history.csv",
            mime="text/csv"
        )

    with col2:

        confirm = st.checkbox(
            "clear history"
        )

        if confirm:

            if st.button("🗑 Clear History"):

                empty_df = pd.DataFrame(
                    columns=[
                        "Date",
                        "Source",
                        "Target",
                        "Input",
                        "Output"
                    ]
                )

                empty_df.to_csv(
                    history_file,
                    index=False
                )

                st.success(
                    "History cleared successfully!"
                )

                st.rerun()

except FileNotFoundError:

    st.warning(
        "No translation history found."
    )