import tkinter as tk

class Cell:
    """Store an item for a linked list."""
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"


def has_loop_tortoise_and_hare(sentinel):
    """
    Return True if the list has a loop.
    If the list has a loop, break it.
    """
    # Loop through the list.
    tortoise = sentinel
    hare = sentinel.next
    while tortoise != hare:
        # If the hare is at the end of the list, then there is no loop.
        if (hare == None) or (hare.next == None):
            return False

        # Advance the tortoise once and the hare twice.
        tortoise = tortoise.next
        hare = hare.next.next

    # Start the hare over at slow
    # speed until they meet again.
    hare = sentinel
    tortoise = tortoise.next
    while tortoise != hare:
        # Advance the tortoise and hare one cell.
        tortoise = tortoise.next
        hare = hare.next

    # We are at the start of the loop. Find the end.
    while hare.next != tortoise:
        hare = hare.next

    # Break the loop.
    hare.next = None

    # There was a loop.
    return True


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("break_loop_tortoise_and_hare")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x230")

        frame = tk.LabelFrame(self.window, text="List1")
        frame.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        frame.columnconfigure(1, weight=1)
        label = tk.Label(frame, text="Original List:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.original_list1_entry = tk.Entry(frame)
        self.original_list1_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        label = tk.Label(frame, text="Has Loop?")
        label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.has_loop1_entry = tk.Entry(frame)
        self.has_loop1_entry.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        label = tk.Label(frame, text="New List:")
        label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        self.new_list1_entry = tk.Entry(frame)
        self.new_list1_entry.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        frame = tk.LabelFrame(self.window, text="List2")
        frame.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        frame.columnconfigure(1, weight=2)
        label = tk.Label(frame, text="Original List:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.original_list2_entry = tk.Entry(frame)
        self.original_list2_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        label = tk.Label(frame, text="Has Loop?")
        label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.has_loop2_entry = tk.Entry(frame)
        self.has_loop2_entry.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        label = tk.Label(frame, text="New List:")
        label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        self.new_list2_entry = tk.Entry(frame)
        self.new_list2_entry.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        # List 1.
        # Make a list with no loop.
        i1 = Cell("I", None)
        h1 = Cell("H", i1)
        g1 = Cell("G", h1)
        f1 = Cell("F", g1)
        e1 = Cell("E", f1)
        d1 = Cell("D", e1)
        c1 = Cell("C", d1)
        b1 = Cell("B", c1)
        a1 = Cell("A", b1)
        sentinel1 = Cell("", a1)

        # Display the list.
        self.original_list1_entry.insert(0, self.list_to_string(sentinel1, 15))

        # Indicate whether the list has a loop.
        self.has_loop1_entry.insert(0, f"{has_loop_tortoise_and_hare(sentinel1)}")

        # Redisplay the list.
        self.new_list1_entry.insert(0, self.list_to_string(sentinel1, 15))

        # List 2.
        # Make a list with a loop.
        i2 = Cell("I", None)
        h2 = Cell("H", i2)
        g2 = Cell("G", h2)
        f2 = Cell("F", g2)
        e2 = Cell("E", f2)
        d2 = Cell("D", e2)
        c2 = Cell("C", d2)
        b2 = Cell("B", c2)
        a2 = Cell("A", b2)
        sentinel2 = Cell("", a2)
        i2.next = d2

        # Display the list.
        self.original_list2_entry.insert(0, self.list_to_string(sentinel2, 15))

        # Indicate whether the list has a loop.
        self.has_loop2_entry.insert(0, f"{has_loop_tortoise_and_hare(sentinel2)}")

        # Redisplay the list.
        self.new_list2_entry.insert(0, self.list_to_string(sentinel2, 15))

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def list_to_string(self, sentinel, max_cells):
        """ Return a string representation of the list."""
        result = ""
        i = 0
        cell = sentinel.next
        while cell != None:
            result += f"{cell} "
            i += 1
            if i > max_cells:
                break
            cell = cell.next
        return result



if __name__ == '__main__':
    app = App()

# app.root.destroy()
