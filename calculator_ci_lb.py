import tkinter as tk
from tkinter import ttk


class CompoundInterest:
    def __init__(self, parent):
        style = ttk.Style()
        style.configure('TFrame', background='#F0F0F0')
        self.frame = ttk.Frame(parent, style='TFrame')
        self.label = ttk.Label(self.frame, text="Compound Interest Calculator", font="Helvetica, 16")
        self.label.pack()

        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")

        # Create a Principal Amount label
        principal_amount_label = ttk.Label(self.frame, text="Principal Amount:")
        principal_amount_label.pack(side="top")

        # Create Principal amount entry box
        self.principal_amount = ttk.Entry(self.frame, justify="right")
        self.principal_amount.pack(side='top')

        # Create a interest rate label
        interest_rate_label = ttk.Label(self.frame, text="Interest Rate (%) : ")
        interest_rate_label.pack(side="top")

        # Create interest rate entry box
        self.interest_rate = ttk.Entry(self.frame, justify="right")
        self.interest_rate.pack(side='top')

        # Create a Time label
        time_label = ttk.Label(self.frame, text="Time (years) : ")
        time_label.pack(side="top")

        # Create a Time entry box
        self.time_entry = ttk.Entry(self.frame, justify="right")
        self.time_entry.pack(side='top')

        # Create a Number of Times Interest is compounded per year label and Combobox
        self.compound_times_label = ttk.Label(self.frame, text="Number of Times Interest is Compounded Per Year : ")
        self.compound_times_label.pack(side="top")

        self.combo_box = ttk.Combobox(self.frame, values=["Yearly", "Monthly", "Daily"], justify="center")
        self.combo_box.pack(pady=5)

        # Set default value
        self.combo_box.set("Monthly")

        # Bind event to selection
        self.combo_box.bind("<<ComboboxSelected>>", self.on_select)

        # Add Submit button
        submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        submit_button.pack(side="top", expand=True)

        # Create a Compound Interest : label
        compound_interest_label = ttk.Label(self.frame, text="Compound Interest : ")
        compound_interest_label.pack(side="top")

        self.compound_interest = tk.StringVar()
        self.compound_interest_entry = ttk.Entry(self.frame, textvariable=self.compound_interest, justify="right")
        self.compound_interest_entry.pack(side='top')

    def clear_all(self):
        # whole content of entry boxes is deleted
        self.principal_amount.delete(0, tk.END)
        self.interest_rate.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.compound_interest_entry.delete(0, tk.END)

        # set focus on the principal_field entry box
        self.principal_amount.focus_set()

    def calculate(self):
        # Compound Interest Formula
        # A = P(1 + r/n)^(nt)
        # where:
        # A = amount
        # P = principal
        # r = interest rate
        # n = number of times interest is compounded per year
        # t = time in years

        # get a content from entry box
        try:
            principal = float(self.principal_amount.get())
        except ValueError:
            self.principal_amount.delete(0, tk.END)
            return

        try:
            rate = float(self.interest_rate.get())
        except ValueError:
            self.interest_rate.delete(0, tk.END)
            return

        try:
            time = int(self.time_entry.get())
        except ValueError:
            self.time_entry.delete(0, tk.END)
            return

        compound_option = self.combo_box.get()
        if compound_option == "Yearly":
            compound_times_per_year = 1
        elif compound_option == "Daily":
            compound_times_per_year = 365
        else:
            compound_times_per_year = 12

        # Calculate compound interest
        compound_int = principal * (pow((1 + (rate / 100) / compound_times_per_year), compound_times_per_year * time))

        self.compound_interest.set(format(compound_int, '10.2f'))

    def on_select(self, _event):
        selected_item = self.combo_box.get()
        self.compound_times_label.config(text="Number of Times Interest is Compounded Per Year : " + selected_item)


class LoanBalance:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.label = ttk.Label(self.frame, text="Loan Balance Calculator", font="Helvetica, 16")
        self.label.pack()

        # Create a Interest Rate label and entry box
        interest_rate_label = ttk.Label(self.frame, text="Annual Interest Rate")
        interest_rate_label.pack(side="top")
        self.interest_rate = ttk.Entry(self.frame, justify="right")
        self.interest_rate.pack(side='top')

        # Create a Number of Years label and entry box
        years_label = ttk.Label(self.frame, text="Number of Years")
        years_label.pack(side="top")
        self.number_of_years = ttk.Entry(self.frame, justify="right")
        self.number_of_years.pack(side='top')

        # Create a Loan Amount label and entry box
        loan_label = ttk.Label(self.frame, text="Loan Amount")
        loan_label.pack(side="top")
        self.loan_amount = ttk.Entry(self.frame, justify="right")
        self.loan_amount.pack(side='top')

        # Add Compute button
        compute_button = ttk.Button(self.frame, text="Compute Payment", command=self.compute_payment)
        compute_button.pack(side="top", expand=True)

        monthly_label = ttk.Label(self.frame, text="Monthly Payment")
        monthly_label.pack(side="top")
        self.monthly_payment = tk.StringVar()
        self.monthly_payment_entry = ttk.Entry(self.frame, textvariable=self.monthly_payment, justify="right")
        self.monthly_payment_entry.pack(side='top')

        total_label = ttk.Label(self.frame, text="Total Payment")
        total_label.pack(side="top")
        self.total_payment = tk.StringVar()
        self.total_payment_entry = ttk.Entry(self.frame, textvariable=self.total_payment, justify="right")
        self.total_payment_entry.pack(side='top')

    def compute_payment(self):
        """
        Loans Formula
        P0 = d (1 − (1 + r/k) ^ (−Nk)
             ------------------------
                    (r/k)

        P0 is the balance in the account at the beginning (the principal, or amount of the loan).
        d is your loan payment (your monthly payment, annual payment, etc)
        r is the annual interest rate in decimal form.
        k is the number of compounding periods in one year.
        N is the length of the loan, in years
        """

        try:
            loan_amt = float(self.loan_amount.get())
        except ValueError:
            self.loan_amount.delete(0, tk.END)
            return

        try:
            interest_rate = float(self.interest_rate.get())
        except ValueError:
            self.interest_rate.delete(0, tk.END)
            return

        try:
            years = int(self.number_of_years.get())
        except ValueError:
            self.number_of_years.delete(0, tk.END)
            return

        monthly_payment = self.calculate_monthly_payment(loan_amt, interest_rate/1200, years)
        # print("monthly payment is ", monthly_payment)
        self.monthly_payment.set(format(monthly_payment, '10.2f'))

        # use the rounded monthly payment displayed otherwise the
        # total payment may be more than 12 x years of monthly payment
        total_payment = float(self.monthly_payment.get()) * 12 * years
        self.total_payment.set(format(total_payment, '10.2f'))

    @staticmethod
    def calculate_monthly_payment(loan_amount, monthly_interest_rate, number_of_years):
        # compute the monthly payment
        monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / pow((1 + monthly_interest_rate), (number_of_years * 12)))
        return monthly_payment


def main():
    root = tk.Tk()
    root.title("Compound Interest and Loan Balance Calculator")
    root.geometry("500x300")
    root.configure(bg="blue")

    tab_control = ttk.Notebook(root)

    compound_interest = CompoundInterest(tab_control).frame
    loan_balance = LoanBalance(tab_control).frame

    tab_control.add(compound_interest, text='Compound Interest')
    tab_control.add(loan_balance, text='Loan Balance')

    tab_control.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == '__main__':
    main()
