import random

from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Jogador

RANKING_CACHE_KEY = 'ranking_top10'
RANKING_CACHE_TIMEOUT = 60 * 5  # 5 minutos


def _adicionar_linha(request, texto, classe='sistema'):
    historico = request.session.get('historico', [])
    historico.append({'texto': texto, 'classe': classe})
    request.session['historico'] = historico


def jogo_view(request):
    if request.method == 'POST':
        valor = request.POST.get('valor', '').strip()
        estado = request.session.get('estado', 'nome')

        if valor:
            _adicionar_linha(request, f'> {valor}', 'entrada')

        if estado == 'nome':
            nome = valor.title() or 'Jogador'
            request.session['nome'] = nome
            request.session['numero_secreto'] = random.randint(1, 10)
            request.session['tentativas'] = 0
            request.session['estado'] = 'jogando'
            _adicionar_linha(
                request,
                f'{nome}, pensei em um número entre 1 e 10. Tente adivinhar!'
            )

        elif estado == 'fim':
            nome = request.session.get('nome', 'Jogador')
            request.session['numero_secreto'] = random.randint(1, 10)
            request.session['tentativas'] = 0
            request.session['estado'] = 'jogando'
            _adicionar_linha(
                request,
                f'{nome}, pensei em outro número entre 1 e 10. Tente adivinhar!'
            )

        else:  # estado == 'jogando'
            if not valor.isnumeric():
                _adicionar_linha(request, 'Erro! Digite apenas valores inteiros.', 'erro')
            else:
                palpite = int(valor)
                numero_secreto = request.session.get('numero_secreto')
                tentativas = request.session.get('tentativas', 0) + 1
                request.session['tentativas'] = tentativas

                if palpite == numero_secreto:
                    nome = request.session.get('nome', 'Jogador')
                    Jogador.objects.create(nome=nome, pontuacao=tentativas)
                    cache.delete(RANKING_CACHE_KEY)  
                    _adicionar_linha(
                        request,
                        f'Parabéns, {nome}! Você venceu em {tentativas} tentativa(s) '
                        f'— eu pensei no {numero_secreto}.',
                        'sucesso'
                    )
                    _adicionar_linha(request, 'Digite qualquer coisa para jogar novamente.')
                    request.session['estado'] = 'fim'
                elif palpite > numero_secreto:
                    _adicionar_linha(request, 'Errou! O número é menor que esse.', 'dica')
                else:
                    _adicionar_linha(request, 'Errou! O número é maior que esse.', 'dica')

        request.session.modified = True
        #return redirect(f"{reverse('jogo')}#jogoWrapper")

    historico = request.session.get('historico', [])

    ranking = cache.get(RANKING_CACHE_KEY)
    if ranking is None:
        ranking = list(Jogador.objects.all()[:10])
        cache.set(RANKING_CACHE_KEY, ranking, RANKING_CACHE_TIMEOUT)

    contexto = {
        'historico': list(reversed(historico)),
        'ranking': ranking,
    }
    return render(request, 'game/index.html', contexto)


def reiniciar(request):
    """Zera a sessão por completo, como se um novo jogador tivesse chegado."""
    for chave in ('historico', 'estado', 'nome', 'numero_secreto', 'tentativas'):
        request.session.pop(chave, None)
    return redirect(f"{reverse('jogo')}#jogoWrapper")
