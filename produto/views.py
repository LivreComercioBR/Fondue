from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Categoria, Produto, Opcoes, Adicional


def produtos(request):
    # request.session['carrinho'].clear()
    # request.session.save()
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos, 'categorias': categorias, 'carrinho': len(request.session['carrinho'])})


def categorias(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.filter(categoria_id=id)
    categorias = Categoria.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos, 'categorias': categorias, 'carrinho': len(request.session['carrinho'])})


def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto, 'session': len(request.session['carrinho']), 'erro': erro, 'categorias': categorias})


def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)

    def removeLixo():
        adicionais = x.copy()
        adicionais.pop('id')
        adicionais.pop('csrfmiddlewaretoken')
        adicionais.pop('observacoes')
        adicionais.pop('quantidade')
        adicionais = list(adicionais.items())

        return adicionais

    adicionais = removeLixo()

    id = int(x['id'][0])
    preco_total = Produto.objects.filter(id=id)[0].preco
    adicionais_verifica = Adicional.objects.filter(produto=id)
    aprovado = True

    for i in adicionais_verifica:
        encontrou = False
        minimo = i.minimo
        maximo = i.maximo
        for j in adicionais:
            if i.nome == j[0]:
                encontrou = True
                if len(j[1]) < minimo or len(j[1]) > maximo:
                    aprovado = False
        if minimo > 0 and encontrou == False:
            aprovado = False

    if not aprovado:
        return redirect(f'/empresa/produto/{id}?erro=1')

    for i, j in adicionais:
        for k in j:
            preco_total += Opcoes.objects.filter(id=int(k))[0].acrescimo

    def troca_id_por_nome_adicional(adicional):
        adicionais_com_nome = []
        for i in adicionais:
            opcoes = []
            for j in i[1]:
                op = Opcoes.objects.filter(id=int(j))[0].nome
                opcoes.append(op)
            adicionais_com_nome.append((i[0], opcoes))
        return adicionais_com_nome

    adicionais = troca_id_por_nome_adicional(adicionais)

    preco_total *= int(x['quantidade'][0])
    data = {'id_produto': int(x['id'][0]),
            'observacoes': x['observacoes'][0],
            'preco': preco_total,
            'adicionais': adicionais,
            'quantidade': x['quantidade'][0]}

    request.session['carrinho'].append(data)
    request.session.save()
    # return HttpResponse(request.session['carrinho'])
    return redirect(f'/empresa/ver_carrinho')


def ver_carrinho(request):
    # if not request.session.get("carrinho"):
    #     request.session["carrinho"] = []
    #     request.session.save()

    dados_mostrar = []

    categorias = Categoria.objects.all()

    for i in request.session["carrinho"]:
        # print(i)
        # return HttpResponse(request.session["carrinho"])
        prod = Produto.objects.filter(
            id=i["id_produto"])
        # id=list(request.session["carrinho"][0][1]))
        # return HttpResponse(prod)
        dados_mostrar.append(
            {'imagem': prod[0].img.url,
                'nome': prod[0].nome_produto,
                'quantidade': i['quantidade'],
                'preco': i['preco'],
                'id': i['id_produto']
             }
        )

    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'ver_carrinho.html', {'dados': dados_mostrar, 'total': total, 'carrinho': len(request.session['carrinho']), 'categorias': categorias})


def remover_produto(request, id):
    request.session['carrinho'].pop(id)
    request.session.save()
    return redirect('/empresa/ver_carrinho')
