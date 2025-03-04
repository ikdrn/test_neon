from django.shortcuts import render, redirect
from .models import Employee

# ログイン画面用のビュー
def login_view(request):
    context = {}  # テンプレートに渡すコンテキスト（辞書型）
    if request.method == 'POST':
        # POST で送信された emplid を取得し、前後の空白を除去
        emplid = request.POST.get('emplid', '').strip()
        if emplid:
            try:
                # Employee テーブルから、入力された emplid に一致するレコードを取得
                employee = Employee.objects.get(emplid=emplid)
                # ログイン成功の場合、セッションに emplid と emplnm を保存
                request.session['emplid'] = employee.emplid
                request.session['emplnm'] = employee.emplnm
                # 成功ページへリダイレクト
                return redirect('success')
            except Employee.DoesNotExist:
                # 該当する従業員が存在しない場合、エラーメッセージをコンテキストに追加
                context['error'] = 'Invalid emplid'
        else:
            # emplid が入力されなかった場合のエラーメッセージ
            context['error'] = 'Please enter emplid'
    # GET リクエストやエラーがある場合、ログイン画面のテンプレートを表示
    return render(request, 'app/login.html', context)

# ログイン成功後の画面用のビュー
def success_view(request):
    # セッションから emplid と emplnm を取得
    emplid = request.session.get('emplid')
    emplnm = request.session.get('emplnm')
    # セッション情報が不足している場合は、ログインページにリダイレクト
    if not emplid or not emplnm:
        return redirect('login')
    # ログイン成功画面のテンプレートをレンダリングし、セッション情報をコンテキストとして渡す
    return render(request, 'app/success.html', {'emplid': emplid, 'emplnm': emplnm})
