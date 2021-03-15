"""
Fibonacci Spreadsheet example for book.
"""
try:
    import networkx as nx
except ImportError:
    from ch07.graph import Replacement
    nx = Replacement()

def fibonacci_example(ss):
    """Initialize Spreadsheet to small Fibonacci example for book."""
    entries = {
        'A1': 'N',
        'B1': 'Fibn',
        'C1': 'Sn',
        'A2': '0',
        'A3': '=(A2+1)',
        'A4': '=(A3+1)',
        'A5': '=(A4+1)',
#         'A6': '=(A5+1)',
#         'A7': '=(A6+1)',
#         'A8': '=(A7+1)',
        'B2': '0',
        'B3': '1',
        'B4': '=(B2+B3)',
        'B5': '=(B3+B4)',
#         'B6': '=(B4+B5)',
#         'B7': '=(B5+B6)',
#         'B8': '=(B6+B7)',
        'C2': '=B2',
        'C3': '=(B3+C2)',
        'C4': '=(B4+C3)',
        'C5': '=(B5+C4)',
#         'C6': '=(B6+C5)',
#         'C7': '=(B7+C6)',
#         'C8': '=(B8+C7)'        
    }
    for k in entries:
        ss.set(k,entries[k])

#######################################################################
if __name__ == "__main__":
    try:
        import tkinter
        from ch07.spreadsheet import Spreadsheet

        root = tkinter.Tk()
        ss = Spreadsheet(root)
        fibonacci_example(ss)
        from ch07.digraph_search import topological_sort
        print (list(topological_sort(ss.digraph)))
        root.mainloop()
    except (ImportError):
        print('tkinter is not installed so unable to launch spreadsheet application')
