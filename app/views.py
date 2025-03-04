from django.shortcuts import render, redirect
from .models import Employee

def login_view(request):
    context = {}
    if request.method == 'POST':
        emplid = request.POST.get('emplid', '').strip()
        if emplid:
            try:
                # employeesテーブルからemplidに一致するレコードを取得
                employee = Employee.objects.get(emplid=emplid)
                # ログイン成功ならemplidとemplnmをセッションに保存
                request.session['emplid'] = employee.emplid
                request.session['emplnm'] = employee.emplnm
                return redirect('success')
            except Employee.DoesNotExist:
                context['error'] = 'Invalid emplid'
        else:
            context['error'] = 'Please enter emplid'
    return render(request, 'app/login.html', context)

def success_view(request):
    # セッションからemplidとemplnmを取得
    emplid = request.session.get('emplid')
    emplnm = request.session.get('emplnm')
    if not emplid or not emplnm:
        return redirect('login')
    return render(request, 'app/success.html', {'emplid': emplid, 'emplnm': emplnm})