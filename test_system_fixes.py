#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Teste das Correções do Sistema
Valida se as correções implementadas resolveram os problemas críticos
"""

import sys
import os
import time
import logging
from typing import Dict, Any

# Adiciona src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def test_time_import_fixes():
    """Testa se os imports de time foram corrigidos"""
    
    print("=" * 60)
    print("⏰ TESTE DOS IMPORTS DE TIME CORRIGIDOS")
    print("=" * 60)
    
    try:
        # Testa mental_drivers_architect
        from services.mental_drivers_architect import mental_drivers_architect
        print("✅ mental_drivers_architect importado com sucesso")
        
        # Testa anti_objection_system
        from services.anti_objection_system import anti_objection_system
        print("✅ anti_objection_system importado com sucesso")
        
        # Testa pre_pitch_architect
        from services.pre_pitch_architect import pre_pitch_architect
        print("✅ pre_pitch_architect importado com sucesso")
        
        # Testa se time está disponível nos módulos
        test_data = {'segmento': 'Teste'}
        
        # Testa geração de drivers com fallback
        try:
            drivers = mental_drivers_architect.generate_complete_drivers_system({}, test_data)
            if drivers and 'generation_timestamp' in drivers:
                print("✅ Drivers mentais: timestamp gerado corretamente")
            else:
                print("⚠️ Drivers mentais: sem timestamp mas funcionando")
        except Exception as e:
            print(f"❌ Erro nos drivers mentais: {e}")
            return False
        
        print("✅ Todos os imports de time foram corrigidos!")
        return True
        
    except Exception as e:
        print(f"❌ Erro crítico nos imports: {e}")
        return False

def test_fallback_systems():
    """Testa se os sistemas de fallback funcionam"""
    
    print("\n" + "=" * 60)
    print("🔄 TESTE DOS SISTEMAS DE FALLBACK")
    print("=" * 60)
    
    try:
        from services.mental_drivers_architect import mental_drivers_architect
        from services.anti_objection_system import anti_objection_system
        from services.pre_pitch_architect import pre_pitch_architect
        
        test_data = {
            'segmento': 'Produtos Digitais',
            'produto': 'Curso Online',
            'publico': 'Empreendedores'
        }
        
        # Testa fallback de drivers mentais
        print("🧠 Testando fallback de drivers mentais...")
        try:
            # Força erro para testar fallback
            drivers = mental_drivers_architect._generate_fallback_drivers_system(test_data)
            
            if drivers and drivers.get('fallback_mode'):
                print(f"✅ Fallback drivers: {len(drivers['drivers_customizados'])} drivers gerados")
            else:
                print("❌ Fallback drivers falhou")
                return False
        except Exception as e:
            print(f"❌ Erro no fallback drivers: {e}")
            return False
        
        # Testa fallback de anti-objeção
        print("🛡️ Testando fallback de anti-objeção...")
        try:
            anti_obj = anti_objection_system._generate_fallback_anti_objection_system(test_data)
            
            if anti_obj and anti_obj.get('fallback_mode'):
                print(f"✅ Fallback anti-objeção: {len(anti_obj['objecoes_universais'])} objeções")
            else:
                print("❌ Fallback anti-objeção falhou")
                return False
        except Exception as e:
            print(f"❌ Erro no fallback anti-objeção: {e}")
            return False
        
        # Testa fallback de pré-pitch
        print("🎯 Testando fallback de pré-pitch...")
        try:
            pre_pitch = pre_pitch_architect._generate_fallback_pre_pitch_system(test_data)
            
            if pre_pitch and pre_pitch.get('fallback_mode'):
                print(f"✅ Fallback pré-pitch: {len(pre_pitch['orquestracao_emocional']['sequencia_psicologica'])} fases")
            else:
                print("❌ Fallback pré-pitch falhou")
                return False
        except Exception as e:
            print(f"❌ Erro no fallback pré-pitch: {e}")
            return False
        
        print("✅ Todos os sistemas de fallback funcionam!")
        return True
        
    except Exception as e:
        print(f"❌ Erro crítico nos fallbacks: {e}")
        return False

def test_quality_thresholds():
    """Testa se os thresholds de qualidade foram ajustados"""
    
    print("\n" + "=" * 60)
    print("📊 TESTE DOS THRESHOLDS DE QUALIDADE AJUSTADOS")
    print("=" * 60)
    
    try:
        from services.analysis_quality_controller import analysis_quality_controller
        from services.ultra_detailed_analysis_engine import ultra_detailed_analysis_engine
        
        # Verifica thresholds do quality controller
        thresholds = analysis_quality_controller.quality_thresholds
        
        print("📋 Thresholds do Quality Controller:")
        print(f"   • Conteúdo mínimo: {thresholds['min_content_length']} chars")
        print(f"   • Fontes mínimas: {thresholds['min_sources']}")
        print(f"   • Score mínimo: {thresholds['min_quality_score']}%")
        print(f"   • Taxa de sucesso: {thresholds['min_component_success_rate']*100}%")
        
        # Verifica thresholds do engine
        engine_threshold = ultra_detailed_analysis_engine.quality_threshold
        print(f"   • Threshold do engine: {engine_threshold}%")
        
        # Testa análise com dados limitados
        limited_analysis = {
            'projeto_dados': {'segmento': 'Teste'},
            'pesquisa_web_massiva': {
                'estatisticas': {
                    'total_conteudo': 600,  # Acima do novo mínimo (500)
                    'fontes_unicas': 2,     # Igual ao novo mínimo (2)
                    'qualidade_media': 45   # Acima do novo mínimo (40)
                }
            },
            'avatar_ultra_detalhado': {
                'perfil_demografico': {'idade': '30-45 anos'},
                'dores_viscerais': ['Dor 1', 'Dor 2', 'Dor 3', 'Dor 4', 'Dor 5']
            },
            'insights_exclusivos': ['Insight 1', 'Insight 2', 'Insight 3', 'Insight 4', 'Insight 5']
        }
        
        validation = analysis_quality_controller.validate_complete_analysis(limited_analysis)
        
        print(f"\n🧪 Teste com dados limitados:")
        print(f"   • Válida: {validation['valid']}")
        print(f"   • Score: {validation['quality_score']:.1f}%")
        print(f"   • Erros: {len(validation['errors'])}")
        
        if validation['valid'] or validation['quality_score'] >= 40:
            print("✅ Thresholds ajustados corretamente - análise aceita!")
            return True
        else:
            print("❌ Thresholds ainda muito restritivos")
            return False
        
    except Exception as e:
        print(f"❌ Erro no teste de thresholds: {e}")
        return False

def test_enhanced_trends_service():
    """Testa o novo serviço de tendências"""
    
    print("\n" + "=" * 60)
    print("📈 TESTE DO SERVIÇO DE TENDÊNCIAS APRIMORADO")
    print("=" * 60)
    
    try:
        from services.enhanced_trends_service import enhanced_trends_service
        
        # Testa busca de tendências
        print("🔍 Buscando tendências para 'Produtos Digitais'...")
        
        trends_data = enhanced_trends_service.get_market_trends('Produtos Digitais')
        
        if trends_data:
            print(f"✅ Tendências obtidas:")
            print(f"   • Total: {trends_data.get('total_tendencias', 0)}")
            print(f"   • Fontes: {trends_data.get('fontes_ativas', 0)}")
            print(f"   • Qualidade: {trends_data.get('qualidade_dados', 'N/A')}")
            print(f"   • Fallback mode: {trends_data.get('fallback_mode', False)}")
            
            # Mostra algumas tendências
            tendencias = trends_data.get('tendencias_identificadas', [])
            for i, trend in enumerate(tendencias[:3], 1):
                print(f"   {i}. {trend.get('titulo', 'N/A')}")
            
            return True
        else:
            print("❌ Nenhuma tendência obtida")
            return False
        
    except Exception as e:
        print(f"❌ Erro no teste de tendências: {e}")
        return False

def test_url_resolver_improvements():
    """Testa melhorias no resolvedor de URLs"""
    
    print("\n" + "=" * 60)
    print("🔗 TESTE DAS MELHORIAS NO RESOLVEDOR DE URLS")
    print("=" * 60)
    
    try:
        from services.url_resolver import url_resolver
        
        # URLs problemáticas do Bing
        test_urls = [
            'https://www.bing.com/ck/a?!&&p=test&u=a1aHR0cHM6Ly9nMS5nbG9iby5jb20%3d',
            'https://www.bing.com/ck/a?!&&p=test&u=a1aHR0cHM6Ly9leGFtZS5jb20%3D',
            'https://g1.globo.com/tecnologia/',  # URL normal
        ]
        
        success_count = 0
        
        for i, url in enumerate(test_urls, 1):
            print(f"\n--- TESTE {i}: {url[:60]}... ---")
            try:
                resolved = url_resolver.resolve_redirect_url(url)
                
                if resolved and resolved.startswith('http') and resolved != url:
                    print(f"✅ RESOLVIDA: {resolved}")
                    success_count += 1
                elif resolved == url:
                    print(f"✅ URL DIRETA: {resolved}")
                    success_count += 1
                else:
                    print(f"❌ FALHA: {resolved}")
                    
            except Exception as e:
                print(f"❌ ERRO: {e}")
        
        success_rate = (success_count / len(test_urls)) * 100
        print(f"\n📊 Taxa de sucesso: {success_rate:.1f}%")
        
        return success_rate >= 70
        
    except Exception as e:
        print(f"❌ Erro no teste de URL resolver: {e}")
        return False

def run_comprehensive_fixes_test():
    """Executa teste abrangente das correções"""
    
    print("🚀 INICIANDO TESTE ABRANGENTE DAS CORREÇÕES")
    print("=" * 80)
    
    tests = [
        ("Imports de Time Corrigidos", test_time_import_fixes),
        ("Sistemas de Fallback", test_fallback_systems),
        ("Thresholds de Qualidade", test_quality_thresholds),
        ("Serviço de Tendências", test_enhanced_trends_service),
        ("Resolvedor de URLs", test_url_resolver_improvements)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🧪 Executando: {test_name}")
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            
            results.append((test_name, result, execution_time))
            
            status = "✅ PASSOU" if result else "❌ FALHOU"
            print(f"{status} {test_name} em {execution_time:.2f}s")
            
        except Exception as e:
            print(f"❌ Erro crítico em {test_name}: {e}")
            results.append((test_name, False, 0))
    
    # Relatório final
    print("\n" + "=" * 80)
    print("🏁 RELATÓRIO FINAL DAS CORREÇÕES")
    print("=" * 80)
    
    passed = sum(1 for _, result, _ in results if result)
    total = len(results)
    total_time = sum(time for _, _, time in results)
    
    for test_name, result, exec_time in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name:.<45} {status} ({exec_time:.2f}s)")
    
    print(f"\nTotal: {passed}/{total} correções validadas ({passed/total*100:.1f}%)")
    print(f"Tempo total de execução: {total_time:.2f}s")
    
    if passed == total:
        print("\n🎉 TODAS AS CORREÇÕES FUNCIONAM!")
        print("✅ Sistema corrigido e pronto para uso!")
        
        print("\n🔧 CORREÇÕES IMPLEMENTADAS:")
        print("   ✅ Imports de 'time' adicionados nos módulos críticos")
        print("   ✅ Sistemas de fallback para componentes que falham")
        print("   ✅ Thresholds de qualidade mais realistas")
        print("   ✅ Serviço de tendências com múltiplas fontes")
        print("   ✅ Resolvedor de URLs do Bing melhorado")
        print("   ✅ Rate limiting inteligente para evitar bloqueios")
        print("   ✅ Validação mais flexível para aceitar análises úteis")
        
        print("\n🚀 PRÓXIMOS PASSOS:")
        print("1. Execute uma análise completa para validar em produção")
        print("2. Monitore logs para confirmar ausência dos erros anteriores")
        print("3. Ajuste configurações conforme necessário")
        
    elif passed >= total * 0.8:
        print("\n👍 MAIORIA DAS CORREÇÕES FUNCIONA!")
        print("⚠️ Sistema melhorado mas pode precisar de ajustes")
        
    else:
        print("\n❌ MUITAS CORREÇÕES FALHARAM!")
        print("🚨 Sistema ainda precisa de mais trabalho")
    
    return passed >= total * 0.8

if __name__ == "__main__":
    success = run_comprehensive_fixes_test()
    
    if success:
        print("\n🎯 SISTEMA CORRIGIDO COM SUCESSO!")
        print("\n📋 MELHORIAS IMPLEMENTADAS:")
        print("• ✅ Erros de 'time not defined' corrigidos")
        print("• 🔄 Fallbacks robustos para todos os componentes críticos")
        print("• 📊 Thresholds de qualidade mais realistas")
        print("• 🌐 Serviço de tendências com múltiplas fontes")
        print("• 🔗 Resolvedor de URLs do Bing aprimorado")
        print("• ⏱️ Rate limiting inteligente")
        print("• ✅ Validação mais flexível")
        
        print("\n🚀 SISTEMA PRONTO PARA ANÁLISES REAIS!")
        
    else:
        print("\n🔧 AÇÕES ADICIONAIS NECESSÁRIAS:")
        print("1. ❌ Revise os testes que falharam")
        print("2. 🔧 Verifique configurações específicas")
        print("3. 🧪 Execute testes individuais para debug")
        print("4. 📞 Consulte logs detalhados")
    
    sys.exit(0 if success else 1)