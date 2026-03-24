import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

def run_query(code):
    # Simple Security Check
    forbidden = ["import", "__", "os.", "sys.", "open("]
    code_lower = code.lower()
    if any(word in code_lower for word in forbidden):
        return "Unsafe query detected!"

    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)
        return local_vars.get("result", "No result returned")
    except Exception as e:
        if "out-of-bounds" in str(e):
            return None
        return f"Error executing query: {e}"