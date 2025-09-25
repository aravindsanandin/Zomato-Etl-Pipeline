Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """C:\Users\Aravind\anaconda3\Scripts\activate.bat"" etlapp & streamlit run C:\Users\Aravind\OneDrive\Desktop\bangalore-restaurants-etl\streamlit_app.py", 1, True
