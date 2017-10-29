from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from .models import Account, Category, Transaction, TransactionComment

# =================================================================
# Accounts / Dashboard
# =================================================================

class Dashboard(LoginRequiredMixin, View):
	template_name = "dashboard.html"

	@staticmethod
	def expenses_by_category():
		"""Obtain expenses by the category, returns a queryset."""
		categories = Category.objects.filter(type=0)
		categories = categories.annotate(total_amount=Sum('transaction__amount')).order_by('total_amount')
		categories = categorie[:5]
		return categories

	@staticmethod
	def incomes_by_category():
		"""Obtain incomes by the category, returns a queryset."""
		categories = Category.objects.all(type=1)
		categories = categories.annotate(total_amount=Sum('transaction__amount')).order_by('total_amount')
		return categories

	def get(self, request):
		number_of_registers = 5
		accounts_qs = Accounts.objects.filter(is_active=True).order_by('timestamp')[:number_of_registers]
		accounts_qs = accounts_qs.annotate(total_amount=Sum('transaction__amount'))
		transactions_accounts = Transaction.objects.filter(account__in=accounts_qs).order_by('-timestamp')[:number_of_registers]
		expense_categories = self.expenses_by_category()
		income_categories = self.incomes_by_category()
		ctx = {
			'accounts':accounts,
			'expense_categories':expense_categories,
			'income_categories':income_categories,
			'transactions':transactions_accounts,
		}
		return render(request, self.template_name, ctx)

class AccountList(LoginRequiredMixin, ListView):
	template_name = "account_list.html"
	model = Account
	paginate_by = 10

class AccountNew(LoginRequiredMixin, CreateView):
	template_name = "account_new.html"
	model = Account
	fields = ['name', 'description']
	success_url = reverse_lazy('')

	def form_valid(self,form):
		messages.success(self.request, response_messages.SAVE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		return super(AccountNew, self).form_valid(form)

class AccountEdit(LoginRequiredMixin, UpdateView):
	template_name = "account_edit.html"
	model = Account
	fields = ['name', 'description']
	success_url = reverse_lazy('')

	def form_valid(self,form):
		messages.success(self.request, response_messages.UPDATE_SUCCESSFULL)
		return super(AccountEdit, self).form_valid(form)

class AccountDelete(LoginRequiredMixin, DeleteView):
	template_name = "account_delete.html"
	model = Account
	success_url = reverse_lazy('')

	def delete(self, request, *args, **kwargs):
		messages.success(request, response_messages.DELETE_SUCCESSFULL)
		return super(AccountDelete, self).delete(request, *args, **kwargs)


# =================================================================
# Categories
# =================================================================

class CategoryList(LoginRequiredMixin, ListView):
    template_name = "category_list.html"
    model = Category
    paginate_by = 10


class CategoryNew(LoginRequiredMixin, CreateView):
    template_name = "category_new.html"
    model = Category
    fields = ['name', 'type']
    success_url = reverse_lazy('flow:category-list')

    def form_valid(self, form):
        messages.success(self.request, response_messages.SAVE_SUCCESSFULL)
        form.instance.created_by = self.request.user
        return super(CategoryNew, self).form_valid(form)


class CategoryEdit(LoginRequiredMixin, UpdateView):
    template_name = "category_new.html"
    model = Category
    fields = ['name', 'type']
    success_url = reverse_lazy('flow:category-list')

    def form_valid(self, form):
        messages.success(self.request, response_messages.UPDATE_SUCCESSFULL)
        return super(CategoryEdit, self).form_valid(form)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    template_name = "category_delete.html"
    model = Category
    success_url = reverse_lazy('flow:category-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, response_messages.DELETE_SUCCESSFULL)
        return super(CategoryDelete, self).delete(request, *args, **kwargs)

# =================================================================
# Transactions
# =================================================================

class TransactionList(LoginRequiredMixin, ListView):
	template_name = "transaction_list.html"
	model = Transaction
	paginate_by = 10

class TransactionNew(LoginRequiredMixin, CreateView):
	template_name = "transaction_create.html"
	model = Transaction
	success_url = reverse_lazy('')
	form_class = TransactionForm

	def form_valid(self, form):
		messages.success(self.request, response_messages.SAVE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		if form.instance.category.type == 0:
			form.instance.amoun = -form.instance.amount
		return super(TransactionNew, self).form_valid(form)

class TransactionEdit(LoginRequiredMixin, UpdateView):
	template_name = "transaction_edit.html"
	model = Transaction
	form_class = TransactionForm
	success_url = reverse_lazy('')

	def form_valid(self, form):
		messages.success(self.request, response_messages.UPDATE_SUCCESSFULL)
		if form.instance.category.type == 0:
			if form.instance.amount > 0:
				form.instance.amount = -form.instance.amount
		else:
			if form.instance.amount < 0:
				form.instance.amount = abs(form.instance.amount)
		return super(TransactionEdit, self).form_valid(form)

class TransactionDelete(LoginRequiredMixin, DeleteView):
	template_name = "transaction_delete.html"
	model = Transaction
	success_url = reverse_lazy('')

	def delete(self, request, *args, **kwargs):
		messages.success(request, response_messages.DELETE_SUCCESSFULL)
		return super(TransactionDelete, self).delete(request, *args, **kwargs)
