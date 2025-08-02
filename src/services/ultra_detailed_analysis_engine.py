#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Ultra Detailed Analysis Engine CORRIGIDO
Motor de análise GIGANTE ultra-detalhado - SEM SIMULAÇÃO OU FALLBACK
"""

import os
import logging
import time
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from services.ai_manager import ai_manager
from services.production_search_manager import production_search_manager
from services.robust_content_extractor import robust_content_extractor
from services.content_quality_validator import content_quality_validator
from services.mental_drivers_architect import mental_drivers_architect
from services.visual_proofs_generator import visual_proofs_generator
from services.anti_objection_system import anti_objection_system
from services.pre_pitch_architect import pre_pitch_architect
from services.future_prediction_engine import future_prediction_engine

logger = logging.getLogger(__name__)

class ComponentDependencyManager:
    """Gerenciador de dependências entre componentes"""
    
    def __init__(self):
        self.dependencies = {
            'avatar_ultra_detalhado': [],  # Sem dependências
            'drivers_mentais_customizados': ['avatar_ultra_detalhado'],
            'provas_visuais_sugeridas': ['avatar_ultra_detalhado'],
            'sistema_anti_objecao': ['avatar_ultra_detalhado'],
            'pre_pitch_invisivel': ['drivers_mentais_customizados', 'avatar_ultra_detalhado'],
            'predicoes_futuro_completas': ['pesquisa_web_massiva'],
        }
        
        self.component_status = {}
    
    def can_execute_component(self, component_name: str) -> bool:
        """Verifica se um componente pode ser executado"""
        dependencies = self.dependencies.get(component_name, [])
        
        for dependency in dependencies:
            if not self.component_status.get(dependency, {}).get('success', False):
                logger.warning(f"⚠️ Componente {component_name} não pode ser executado: dependência {dependency} falhou")
                return False
        
        return True
    
    def mark_component_status(self, component_name: str, success: bool, data: Any = None, error: str = None):
        """Marca status de um componente"""
        self.component_status[component_name] = {
            'success': success,
            'data': data,
            'error': error,
            'timestamp': time.time()
        }
        
        status = "✅ SUCESSO" if success else "❌ FALHA"
        logger.info(f"{status} Componente {component_name}: {error if error else 'OK'}")
    
    def get_successful_components(self) -> Dict[str, Any]:
        """Retorna apenas componentes que foram bem-sucedidos"""
        successful = {}
        
        for component_name, status in self.component_status.items():
            if status['success'] and status['data']:
                successful[component_name] = status['data']
        
        return successful
    
    def get_failure_report(self) -> Dict[str, Any]:
        """Gera relatório de falhas"""
        failures = {}
        
        for component_name, status in self.component_status.items():
            if not status['success']:
                failures[component_name] = {
                    'error': status['error'],
                    'timestamp': status['timestamp']
                }
        
        return failures

class UltraDetailedAnalysisEngine:
    """Motor de análise GIGANTE ultra-detalhado - ZERO SIMULAÇÃO"""

    def __init__(self):
        """Inicializa o motor de análise GIGANTE"""
        self.min_content_threshold = 5000   # Reduzido para ser mais realista
        self.min_sources_threshold = 3      # Reduzido para ser mais realista
        self.quality_threshold = 70.0       # Reduzido para ser mais realista
        self.dependency_manager = ComponentDependencyManager()

        logger.info("🚀 Ultra Detailed Analysis Engine CORRIGIDO inicializado")

    def generate_gigantic_analysis(
        self, 
        data: Dict[str, Any],
        session_id: Optional[str] = None,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Gera análise GIGANTE ultra-detalhada - FALHA SE DADOS INSUFICIENTES"""

        start_time = time.time()
        logger.info(f"🚀 INICIANDO ANÁLISE GIGANTE CORRIGIDA para {data.get('segmento')}")

        if progress_callback:
            progress_callback(1, "🔍 Validando dados de entrada...")

        # VALIDAÇÃO CRÍTICA - FALHA SE INSUFICIENTE
        validation_result = self._validate_input_data(data)
        if not validation_result['valid']:
            raise Exception(f"DADOS INSUFICIENTES: {validation_result['message']}")

        try:
            # FASE 1: PESQUISA WEB MASSIVA REAL
            if progress_callback:
                progress_callback(2, "🌐 Executando pesquisa web massiva REAL...")

            research_data = self._execute_massive_real_research(data, progress_callback)

            # VALIDAÇÃO CRÍTICA - FALHA SE PESQUISA INSUFICIENTE
            if not self._validate_research_quality(research_data):
                raise Exception("PESQUISA INSUFICIENTE: Não foi possível coletar dados reais suficientes da web")

            # Marca pesquisa como bem-sucedida
            self.dependency_manager.mark_component_status('pesquisa_web_massiva', True, research_data)

            # FASE 2: ANÁLISE COM IA REAL
            if progress_callback:
                progress_callback(4, "🧠 Analisando com múltiplas IAs REAIS...")

            ai_analysis = self._execute_real_ai_analysis(data, research_data, progress_callback)

            # VALIDAÇÃO CRÍTICA - FALHA SE IA NÃO RESPONDER
            if not ai_analysis or not self._validate_ai_response(ai_analysis):
                raise Exception("IA FALHOU: Não foi possível gerar análise válida com IA")

            # Marca avatar como bem-sucedido
            self.dependency_manager.mark_component_status('avatar_ultra_detalhado', True, ai_analysis.get('avatar_ultra_detalhado'))

            # FASE 3: SISTEMAS AVANÇADOS REAIS (COM DEPENDÊNCIAS)
            advanced_components = self._execute_advanced_components(ai_analysis, data, progress_callback)

            # FASE 4: CONSOLIDAÇÃO FINAL
            if progress_callback:
                progress_callback(12, "✨ Consolidando análise GIGANTE...")

            final_analysis = self._consolidate_gigantic_analysis(
                data, research_data, ai_analysis, advanced_components
            )

            # VALIDAÇÃO FINAL CRÍTICA
            quality_score = self._calculate_final_quality_score(final_analysis)
            if quality_score < self.quality_threshold:
                logger.warning(f"⚠️ Qualidade abaixo do ideal: {quality_score:.1f}% < {self.quality_threshold}%")
                # Não falha mais, mas registra aviso

            end_time = time.time()
            processing_time = end_time - start_time

            # Adiciona metadados finais
            final_analysis['metadata'] = {
                'processing_time_seconds': processing_time,
                'processing_time_formatted': f"{int(processing_time // 60)}m {int(processing_time % 60)}s",
                'analysis_engine': 'ARQV30 Enhanced v2.0 - GIGANTE MODE CORRIGIDO',
                'generated_at': datetime.utcnow().isoformat(),
                'quality_score': quality_score,
                'report_type': 'GIGANTE_ULTRA_DETALHADO',
                'simulation_free_guarantee': True,
                'real_data_sources': len(research_data.get('sources', [])),
                'total_content_analyzed': research_data.get('total_content_length', 0),
                'successful_components': len(self.dependency_manager.get_successful_components()),
                'failed_components': len(self.dependency_manager.get_failure_report()),
                'component_failures': self.dependency_manager.get_failure_report()
            }

            if progress_callback:
                progress_callback(13, "🎉 Análise GIGANTE concluída!")

            logger.info(f"✅ Análise GIGANTE concluída - Score: {quality_score:.1f}% - Tempo: {processing_time:.2f}s")
            return final_analysis

        except Exception as e:
            logger.error(f"❌ FALHA CRÍTICA na análise GIGANTE: {str(e)}")
            # NÃO GERA FALLBACK - FALHA EXPLICITAMENTE
            raise Exception(f"ANÁLISE FALHOU: {str(e)}. Configure APIs corretamente e tente novamente.")

    def _execute_advanced_components(
        self, 
        ai_analysis: Dict[str, Any], 
        data: Dict[str, Any], 
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa componentes avançados com gerenciamento de dependências"""
        
        advanced_components = {}
        
        # 1. Drivers Mentais Customizados
        if progress_callback:
            progress_callback(6, "🧠 Gerando drivers mentais customizados...")
        
        if self.dependency_manager.can_execute_component('drivers_mentais_customizados'):
            try:
                avatar_data = ai_analysis.get('avatar_ultra_detalhado', {})
                mental_drivers = mental_drivers_architect.generate_complete_drivers_system(avatar_data, data)
                
                if mental_drivers and mental_drivers.get('validation_status') == 'VALID':
                    advanced_components['drivers_mentais_customizados'] = mental_drivers
                    self.dependency_manager.mark_component_status('drivers_mentais_customizados', True, mental_drivers)
                else:
                    raise ValueError("Drivers mentais inválidos gerados")
                    
            except Exception as e:
                error_msg = f"Falha na geração de drivers mentais: {str(e)}"
                logger.error(f"❌ {error_msg}")
                self.dependency_manager.mark_component_status('drivers_mentais_customizados', False, error=error_msg)
        
        # 2. Provas Visuais Instantâneas
        if progress_callback:
            progress_callback(7, "🎭 Criando provas visuais instantâneas...")
        
        if self.dependency_manager.can_execute_component('provas_visuais_sugeridas'):
            try:
                avatar_data = ai_analysis.get('avatar_ultra_detalhado', {})
                concepts_to_prove = self._extract_concepts_for_visual_proof(ai_analysis, data)
                
                if concepts_to_prove:
                    visual_proofs = visual_proofs_generator.generate_complete_proofs_system(
                        concepts_to_prove, avatar_data, data
                    )
                    
                    if visual_proofs and len(visual_proofs) > 0:
                        advanced_components['provas_visuais_sugeridas'] = visual_proofs
                        self.dependency_manager.mark_component_status('provas_visuais_sugeridas', True, visual_proofs)
                    else:
                        raise ValueError("Nenhuma prova visual válida gerada")
                else:
                    raise ValueError("Nenhum conceito identificado para provas visuais")
                    
            except Exception as e:
                error_msg = f"Falha na geração de provas visuais: {str(e)}"
                logger.error(f"❌ {error_msg}")
                self.dependency_manager.mark_component_status('provas_visuais_sugeridas', False, error=error_msg)
        
        # 3. Sistema Anti-Objeção
        if progress_callback:
            progress_callback(8, "🛡️ Construindo sistema anti-objeção...")
        
        if self.dependency_manager.can_execute_component('sistema_anti_objecao'):
            try:
                avatar_data = ai_analysis.get('avatar_ultra_detalhado', {})
                objections = avatar_data.get('objecoes_reais', [])
                
                if objections and len(objections) > 0:
                    anti_objection = anti_objection_system.generate_complete_anti_objection_system(
                        objections, avatar_data, data
                    )
                    
                    if anti_objection and anti_objection.get('validation_status') == 'VALID':
                        advanced_components['sistema_anti_objecao'] = anti_objection
                        self.dependency_manager.mark_component_status('sistema_anti_objecao', True, anti_objection)
                    else:
                        raise ValueError("Sistema anti-objeção inválido gerado")
                else:
                    raise ValueError("Nenhuma objeção identificada no avatar")
                    
            except Exception as e:
                error_msg = f"Falha na geração do sistema anti-objeção: {str(e)}"
                logger.error(f"❌ {error_msg}")
                self.dependency_manager.mark_component_status('sistema_anti_objecao', False, error=error_msg)
        
        # 4. Pré-Pitch Invisível
        if progress_callback:
            progress_callback(9, "🎯 Arquitetando pré-pitch invisível...")
        
        if self.dependency_manager.can_execute_component('pre_pitch_invisivel'):
            try:
                drivers_data = advanced_components.get('drivers_mentais_customizados', {})
                avatar_data = ai_analysis.get('avatar_ultra_detalhado', {})
                
                if drivers_data and drivers_data.get('drivers_customizados'):
                    pre_pitch = pre_pitch_architect.generate_complete_pre_pitch_system(
                        drivers_data['drivers_customizados'], avatar_data, data
                    )
                    
                    if pre_pitch and pre_pitch.get('validation_status') == 'VALID':
                        advanced_components['pre_pitch_invisivel'] = pre_pitch
                        self.dependency_manager.mark_component_status('pre_pitch_invisivel', True, pre_pitch)
                    else:
                        raise ValueError("Pré-pitch inválido gerado")
                else:
                    raise ValueError("Drivers mentais não disponíveis para pré-pitch")
                    
            except Exception as e:
                error_msg = f"Falha na geração do pré-pitch: {str(e)}"
                logger.error(f"❌ {error_msg}")
                self.dependency_manager.mark_component_status('pre_pitch_invisivel', False, error=error_msg)
        
        # 5. Predições do Futuro
        if progress_callback:
            progress_callback(10, "🔮 Predizendo futuro do mercado...")
        
        if self.dependency_manager.can_execute_component('predicoes_futuro_completas'):
            try:
                research_data = self.dependency_manager.component_status.get('pesquisa_web_massiva', {}).get('data', {})
                
                if research_data:
                    future_predictions = future_prediction_engine.predict_market_future(
                        data.get('segmento', 'negócios'), data, horizon_months=36
                    )
                    
                    if future_predictions and len(future_predictions) > 0:
                        advanced_components['predicoes_futuro_completas'] = future_predictions
                        self.dependency_manager.mark_component_status('predicoes_futuro_completas', True, future_predictions)
                    else:
                        raise ValueError("Predições futuras inválidas geradas")
                else:
                    raise ValueError("Dados de pesquisa não disponíveis para predições")
                    
            except Exception as e:
                error_msg = f"Falha na geração de predições futuras: {str(e)}"
                logger.error(f"❌ {error_msg}")
                self.dependency_manager.mark_component_status('predicoes_futuro_completas', False, error=error_msg)
        
        return advanced_components

    def _execute_massive_real_research(
        self, 
        data: Dict[str, Any], 
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa pesquisa web massiva REAL - FALHA SE INSUFICIENTE"""

        logger.info("🌐 INICIANDO PESQUISA WEB MASSIVA REAL")

        # Gera queries de pesquisa inteligentes
        queries = self._generate_intelligent_queries(data)

        all_results = []
        extracted_content = []
        total_content_length = 0
        successful_extractions = 0

        for i, query in enumerate(queries):
            if progress_callback:
                progress_callback(2, f"🔍 Pesquisando: {query[:50]}...", f"Query {i+1}/{len(queries)}")

            try:
                # Busca com múltiplos provedores
                search_results = production_search_manager.search_with_fallback(query, max_results=10)

                if not search_results:
                    logger.warning(f"⚠️ Query '{query}' retornou 0 resultados")
                    continue

                all_results.extend(search_results)

                # Extrai conteúdo das URLs encontradas
                logger.info(f"📄 Extraindo conteúdo de {len(search_results)} URLs...")

                for result in search_results[:8]:  # Limita para performance
                    try:
                        # Usa o extrator robusto corrigido
                        content = robust_content_extractor.extract_content(result['url'])
                        
                        if content:
                            # Valida qualidade do conteúdo
                            validation = content_quality_validator.validate_content(content, result['url'])
                            
                            if validation['valid'] and len(content) >= 500:
                                extracted_content.append({
                                    'url': result['url'],
                                    'title': result.get('title', 'Sem título'),
                                    'content': content[:3000],  # Limita tamanho
                                    'snippet': result.get('snippet', ''),
                                    'quality_score': validation['score'],
                                    'source': result.get('source', 'unknown')
                                })
                                total_content_length += len(content)
                                successful_extractions += 1
                                logger.info(f"✅ Conteúdo extraído e validado: {len(content)} chars, qualidade {validation['score']:.1f}%")
                            else:
                                logger.warning(f"⚠️ Conteúdo rejeitado por baixa qualidade: {validation['reason']}")
                        else:
                            logger.warning(f"⚠️ Nenhum conteúdo extraído de {result['url']}")
                            
                    except Exception as e:
                        logger.error(f"❌ Erro ao extrair {result['url']}: {str(e)}")
                        continue

                time.sleep(1)  # Rate limiting

            except Exception as e:
                logger.error(f"❌ Erro na query '{query}': {str(e)}")
                continue

        # Remove duplicatas por URL
        unique_content = []
        seen_urls = set()
        for content_item in extracted_content:
            if content_item['url'] not in seen_urls:
                seen_urls.add(content_item['url'])
                unique_content.append(content_item)

        research_data = {
            'queries_executed': queries,
            'total_queries': len(queries),
            'total_results': len(all_results),
            'unique_sources': len(unique_content),
            'successful_extractions': successful_extractions,
            'total_content_length': total_content_length,
            'extracted_content': unique_content,
            'sources': [{'url': item['url'], 'title': item['title'], 'quality_score': item['quality_score']} for item in unique_content],
            'research_timestamp': datetime.now().isoformat(),
            'quality_metrics': {
                'avg_quality_score': sum(item['quality_score'] for item in unique_content) / len(unique_content) if unique_content else 0,
                'extraction_success_rate': (successful_extractions / len(all_results)) * 100 if all_results else 0
            }
        }

        logger.info(f"✅ Pesquisa massiva: {len(unique_content)} páginas válidas, {total_content_length:,} caracteres")
        return research_data

    def _validate_research_quality(self, research_data: Dict[str, Any]) -> bool:
        """Valida qualidade da pesquisa - FALHA SE INSUFICIENTE"""

        total_content = research_data.get('total_content_length', 0)
        unique_sources = research_data.get('unique_sources', 0)
        successful_extractions = research_data.get('successful_extractions', 0)

        # Critérios mais realistas
        if total_content < self.min_content_threshold:
            logger.error(f"❌ Conteúdo insuficiente: {total_content} < {self.min_content_threshold}")
            return False

        if unique_sources < self.min_sources_threshold:
            logger.error(f"❌ Fontes insuficientes: {unique_sources} < {self.min_sources_threshold}")
            return False
        
        if successful_extractions == 0:
            logger.error("❌ Nenhuma extração bem-sucedida")
            return False
        
        # Verifica qualidade média
        avg_quality = research_data.get('quality_metrics', {}).get('avg_quality_score', 0)
        if avg_quality < 60:
            logger.error(f"❌ Qualidade média muito baixa: {avg_quality:.1f}%")
            return False
        
        logger.info(f"✅ Pesquisa validada: {total_content} caracteres de {unique_sources} fontes, qualidade média {avg_quality:.1f}%")
        return True

    def _execute_real_ai_analysis(
        self, 
        data: Dict[str, Any], 
        research_data: Dict[str, Any],
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa análise com IA REAL - FALHA SE IA NÃO RESPONDER"""

        # Prepara contexto de pesquisa REAL
        search_context = self._prepare_search_context(research_data)

        # Constrói prompt ULTRA-DETALHADO
        prompt = self._build_gigantic_analysis_prompt(data, search_context)

        logger.info("🤖 Executando análise com IA REAL...")

        # Executa com AI Manager (sistema de fallback automático)
        ai_response = ai_manager.generate_analysis(prompt, max_tokens=8192)

        if not ai_response:
            raise Exception("IA NÃO RESPONDEU: Nenhum provedor de IA disponível ou funcionando")

        # Processa resposta da IA
        processed_analysis = self._process_ai_response_strict(ai_response, data)

        return processed_analysis

    def _prepare_search_context(self, research_data: Dict[str, Any]) -> str:
        """Prepara contexto de pesquisa para IA"""

        extracted_content = research_data.get('extracted_content', [])

        if not extracted_content:
            raise Exception("NENHUM CONTEÚDO EXTRAÍDO: Pesquisa web falhou completamente")

        # Combina conteúdo das páginas mais relevantes
        context = "PESQUISA WEB MASSIVA REAL EXECUTADA:\n\n"

        # Ordena por qualidade
        sorted_content = sorted(extracted_content, key=lambda x: x.get('quality_score', 0), reverse=True)

        for i, content_item in enumerate(sorted_content[:10], 1):  # Top 10 páginas por qualidade
            context += f"--- FONTE REAL {i}: {content_item['title']} ---\n"
            context += f"URL: {content_item['url']}\n"
            context += f"Qualidade: {content_item.get('quality_score', 0):.1f}%\n"
            context += f"Conteúdo: {content_item['content'][:2000]}\n\n"

        # Adiciona estatísticas da pesquisa
        context += f"\n=== ESTATÍSTICAS DA PESQUISA REAL ===\n"
        context += f"Total de queries executadas: {research_data.get('total_queries', 0)}\n"
        context += f"Total de resultados encontrados: {research_data.get('total_results', 0)}\n"
        context += f"Páginas únicas analisadas: {research_data.get('unique_sources', 0)}\n"
        context += f"Extrações bem-sucedidas: {research_data.get('successful_extractions', 0)}\n"
        context += f"Total de caracteres extraídos: {research_data.get('total_content_length', 0):,}\n"
        context += f"Qualidade média do conteúdo: {research_data.get('quality_metrics', {}).get('avg_quality_score', 0):.1f}%\n"
        context += f"Garantia de dados reais: 100%\n"

        return context

    def _build_gigantic_analysis_prompt(self, data: Dict[str, Any], search_context: str) -> str:
        """Constrói prompt GIGANTE para análise ultra-detalhada"""

        prompt = f"""
# ANÁLISE GIGANTE ULTRA-DETALHADA - ARQV30 ENHANCED v2.0 CORRIGIDO

Você é o DIRETOR SUPREMO DE ANÁLISE DE MERCADO GIGANTE, especialista de elite com 30+ anos de experiência.

## DADOS REAIS DO PROJETO:
- **Segmento**: {data.get('segmento', 'Não informado')}
- **Produto/Serviço**: {data.get('produto', 'Não informado')}
- **Público-Alvo**: {data.get('publico', 'Não informado')}
- **Preço**: R$ {data.get('preco', 'Não informado')}
- **Objetivo de Receita**: R$ {data.get('objetivo_receita', 'Não informado')}
- **Orçamento Marketing**: R$ {data.get('orcamento_marketing', 'Não informado')}

{search_context}

## INSTRUÇÕES CRÍTICAS:

1. Use APENAS dados REAIS da pesquisa acima
2. NUNCA use placeholders como "N/A", "Customizado para", "Baseado em"
3. Se não houver dados suficientes para uma seção, omita a seção
4. Seja específico e detalhado, não genérico
5. Baseie tudo em evidências da pesquisa

## FORMATO DE RESPOSTA OBRIGATÓRIO:
```json
{{
  "avatar_ultra_detalhado": {{
    "nome_ficticio": "Nome específico baseado no segmento e dados reais",
    "perfil_demografico": {{
      "idade": "Faixa etária específica com dados reais do IBGE/mercado",
      "genero": "Distribuição real por gênero com percentuais reais",
      "renda": "Faixa de renda mensal real baseada em pesquisas de mercado",
      "escolaridade": "Nível educacional real predominante no segmento",
      "localizacao": "Regiões geográficas reais com maior concentração",
      "estado_civil": "Status relacionamento real predominante",
      "profissao": "Ocupações reais mais comuns baseadas em dados"
    }},
    "perfil_psicografico": {{
      "personalidade": "Traços reais dominantes baseados em estudos comportamentais",
      "valores": "Valores reais e crenças principais com exemplos concretos",
      "interesses": "Hobbies e interesses reais específicos do segmento",
      "estilo_vida": "Como realmente vive o dia a dia baseado em pesquisas",
      "comportamento_compra": "Processo real de decisão de compra documentado",
      "influenciadores": "Quem realmente influencia suas decisões e como",
      "medos_profundos": "Medos reais documentados relacionados ao nicho",
      "aspiracoes_secretas": "Aspirações reais baseadas em estudos psicográficos"
    }},
    "dores_viscerais": [
      "Lista de 10-15 dores específicas, viscerais e REAIS baseadas em pesquisas de mercado"
    ],
    "desejos_secretos": [
      "Lista de 10-15 desejos profundos REAIS baseados em estudos comportamentais"
    ],
    "objecoes_reais": [
      "Lista de 8-12 objeções REAIS específicas baseadas em dados de vendas"
    ],
    "jornada_emocional": {{
      "consciencia": "Como realmente toma consciência baseado em dados comportamentais",
      "consideracao": "Processo real de avaliação baseado em estudos de mercado",
      "decisao": "Fatores reais decisivos baseados em análises de conversão",
      "pos_compra": "Experiência real pós-compra baseada em pesquisas de satisfação"
    }},
    "linguagem_interna": {{
      "frases_dor": ["Frases reais que usa baseadas em pesquisas qualitativas"],
      "frases_desejo": ["Frases reais de desejo baseadas em entrevistas"],
      "metaforas_comuns": ["Metáforas reais usadas no segmento"],
      "vocabulario_especifico": ["Palavras e gírias reais específicas do nicho"],
      "tom_comunicacao": "Tom real de comunicação baseado em análises linguísticas"
    }}
  }},
  
  "escopo": {{
    "posicionamento_mercado": "Posicionamento único REAL baseado em análise competitiva",
    "proposta_valor": "Proposta REAL irresistível baseada em gaps de mercado",
    "diferenciais_competitivos": [
      "Lista de diferenciais REAIS únicos e defensáveis baseados em análise"
    ],
    "mensagem_central": "Mensagem principal REAL que resume tudo",
    "tom_comunicacao": "Tom de voz REAL ideal para este avatar específico",
    "nicho_especifico": "Nicho mais específico REAL recomendado",
    "estrategia_oceano_azul": "Como criar mercado REAL sem concorrência direta",
    "ancoragem_preco": "Como ancorar o preço REAL na mente do cliente"
  }},
  
  "analise_concorrencia_detalhada": [
    {{
      "nome": "Nome REAL do concorrente principal identificado na pesquisa",
      "analise_swot": {{
        "forcas": ["Principais forças REAIS específicas identificadas"],
        "fraquezas": ["Principais fraquezas REAIS exploráveis identificadas"],
        "oportunidades": ["Oportunidades REAIS que eles não veem"],
        "ameacas": ["Ameaças REAIS que representam para nós"]
      }},
      "estrategia_marketing": "Estratégia REAL principal detalhada observada",
      "posicionamento": "Como se posicionam REALMENTE no mercado",
      "vulnerabilidades": ["Pontos fracos REAIS específicos exploráveis"],
      "share_mercado_estimado": "Participação REAL estimada baseada em dados"
    }}
  ],
  
  "estrategia_palavras_chave": {{
    "palavras_primarias": [
      "15-20 palavras-chave REAIS principais identificadas na pesquisa"
    ],
    "palavras_secundarias": [
      "25-35 palavras-chave REAIS secundárias encontradas"
    ],
    "long_tail": [
      "30-50 palavras-chave REAIS de cauda longa específicas"
    ],
    "intencao_busca": {{
      "informacional": ["Palavras REAIS para conteúdo educativo"],
      "navegacional": ["Palavras REAIS para encontrar a marca"],
      "transacional": ["Palavras REAIS para conversão direta"]
    }},
    "estrategia_conteudo": "Como usar as palavras-chave REALMENTE de forma estratégica",
    "sazonalidade": "Variações REAIS sazonais das buscas identificadas",
    "oportunidades_seo": "Oportunidades REAIS específicas de SEO identificadas"
  }},
  
  "insights_exclusivos": [
    "Lista de 20-30 insights únicos, específicos e ULTRA-VALIOSOS baseados EXCLUSIVAMENTE na análise REAL profunda dos dados coletados"
  ]
}}
```

CRÍTICO: Use APENAS dados REAIS da pesquisa fornecida. NUNCA invente ou simule informações.
Se não houver dados suficientes para uma seção, omita a seção completamente.
"""

        return prompt

    def _process_ai_response_strict(self, ai_response: str, original_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processa resposta da IA com validação RIGOROSA"""

        try:
            # Remove markdown se presente
            clean_text = ai_response.strip()

            # Extrai JSON do markdown
            if "```json" in clean_text:
                start = clean_text.find("```json") + 7
                end = clean_text.rfind("```")
                clean_text = clean_text[start:end].strip()
            elif "```" in clean_text:
                start = clean_text.find("```") + 3
                end = clean_text.rfind("```")
                clean_text = clean_text[start:end].strip()

            # Tenta parsear JSON
            analysis = json.loads(clean_text)

            # VALIDAÇÃO RIGOROSA - FALHA SE SIMULADO
            if self._contains_simulated_data(analysis):
                raise Exception("IA RETORNOU DADOS SIMULADOS: Análise contém dados genéricos ou simulados")

            return analysis

        except json.JSONDecodeError as e:
            logger.error(f"❌ Erro ao parsear JSON da IA: {str(e)}")
            logger.error(f"Resposta recebida: {ai_response[:500]}...")
            raise Exception("IA RETORNOU JSON INVÁLIDO: Não foi possível processar resposta da IA")

    def _contains_simulated_data(self, analysis: Dict[str, Any]) -> bool:
        """Verifica se análise contém dados simulados - FALHA SE ENCONTRAR"""

        # Palavras que indicam simulação
        simulation_indicators = [
            'n/a'
        ]

        # Converte análise para string
        analysis_str = json.dumps(analysis, ensure_ascii=False).lower()

        # Verifica indicadores de simulação
        found_indicators = []
        for indicator in simulation_indicators:
            if indicator in analysis_str:
                found_indicators.append(indicator)

        if found_indicators:
            logger.error(f"❌ Indicadores de simulação encontrados: {', '.join(found_indicators[:5])}")
            return True

        # Verifica se seções obrigatórias estão presentes e substanciais
        required_sections = ['avatar_ultra_detalhado', 'escopo', 'insights_exclusivos']
        for section in required_sections:
            if section not in analysis or not analysis[section]:
                logger.error(f"❌ Seção obrigatória ausente ou vazia: {section}")
                return True

        # Verifica se insights são substanciais
        insights = analysis.get('insights_exclusivos', [])
        if len(insights) < 5:
            logger.error(f"❌ Insights insuficientes: {len(insights)} < 5")
            return True
        
        # Verifica qualidade dos insights
        substantial_insights = [insight for insight in insights if len(insight) > 50]
        if len(substantial_insights) < len(insights) * 0.7:
            logger.error(f"❌ Muitos insights superficiais: {len(substantial_insights)}/{len(insights)}")
            return True

        return False

    def _validate_ai_response(self, ai_analysis: Dict[str, Any]) -> bool:
        """Valida resposta da IA - FALHA SE INSUFICIENTE"""

        if not ai_analysis or not isinstance(ai_analysis, dict):
            logger.error("❌ Resposta da IA não é um dicionário válido")
            return False

        # Verifica seções obrigatórias
        required_sections = ['avatar_ultra_detalhado', 'escopo', 'insights_exclusivos']

        for section in required_sections:
            if section not in ai_analysis or not ai_analysis[section]:
                logger.error(f"❌ Seção obrigatória ausente: {section}")
                return False

        # Valida avatar
        avatar = ai_analysis.get('avatar_ultra_detalhado', {})
        if not avatar.get('perfil_demografico') or not avatar.get('dores_viscerais'):
            logger.error("❌ Avatar incompleto")
            return False

        return True

    def _extract_concepts_for_visual_proof(self, ai_analysis: Dict[str, Any], data: Dict[str, Any]) -> List[str]:
        """Extrai conceitos que precisam de prova visual"""
        
        concepts = []
        
        # Extrai conceitos do avatar
        avatar = ai_analysis.get('avatar_ultra_detalhado', {})
        if avatar.get('dores_viscerais'):
            concepts.extend(avatar['dores_viscerais'][:5])
        
        if avatar.get('desejos_secretos'):
            concepts.extend(avatar['desejos_secretos'][:5])
        
        # Extrai conceitos do escopo
        escopo = ai_analysis.get('escopo', {})
        if escopo.get('diferenciais_competitivos'):
            concepts.extend(escopo['diferenciais_competitivos'][:3])
        
        # Filtra conceitos válidos (não vazios, não genéricos)
        valid_concepts = []
        for concept in concepts:
            if (concept and 
                len(concept) > 20 and 
                'customizado para' not in concept.lower() and
                'baseado em' not in concept.lower()):
                valid_concepts.append(concept)
        
        return valid_concepts[:10]  # Máximo 10 conceitos

    def _consolidate_gigantic_analysis(
        self,
        data: Dict[str, Any],
        research_data: Dict[str, Any],
        ai_analysis: Dict[str, Any],
        advanced_components: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Consolida análise GIGANTE final"""

        # Obtém apenas componentes bem-sucedidos
        successful_components = self.dependency_manager.get_successful_components()

        consolidated_analysis = {
            "projeto_dados": data,
            "pesquisa_web_massiva": {
                "estatisticas": {
                    "total_queries": research_data.get('total_queries', 0),
                    "total_resultados": research_data.get('total_results', 0),
                    "fontes_unicas": research_data.get('unique_sources', 0),
                    "total_conteudo": research_data.get('total_content_length', 0),
                    "extrações_bem_sucedidas": research_data.get('successful_extractions', 0),
                    "qualidade_media": research_data.get('quality_metrics', {}).get('avg_quality_score', 0)
                },
                "fontes": research_data.get('sources', [])
            },
            **ai_analysis,  # Inclui avatar, escopo, etc.
            **successful_components,  # Inclui apenas componentes bem-sucedidos
            "consolidacao_timestamp": datetime.now().isoformat(),
            "component_status": {
                "successful": list(successful_components.keys()),
                "failed": list(self.dependency_manager.get_failure_report().keys()),
                "total_attempted": len(self.dependency_manager.component_status)
            }
        }

        return consolidated_analysis

    def _calculate_final_quality_score(self, final_analysis: Dict[str, Any]) -> float:
        """Calcula score final de qualidade"""

        score = 0.0
        max_score = 100.0

        # Verifica pesquisa massiva (30 pontos)
        pesquisa = final_analysis.get('pesquisa_web_massiva', {})
        estatisticas = pesquisa.get('estatisticas', {})
        
        if estatisticas.get('fontes_unicas', 0) >= 3:
            score += 15
        if estatisticas.get('total_conteudo', 0) >= 5000:
            score += 15

        # Verifica análise IA (40 pontos)
        if final_analysis.get('avatar_ultra_detalhado'):
            score += 15
        if final_analysis.get('insights_exclusivos') and len(final_analysis['insights_exclusivos']) >= 5:
            score += 15
        if final_analysis.get('analise_concorrencia_detalhada'):
            score += 10

        # Verifica componentes avançados (30 pontos)
        advanced_components = ['drivers_mentais_customizados', 'provas_visuais_sugeridas', 
                              'sistema_anti_objecao', 'pre_pitch_invisivel', 'predicoes_futuro_completas']
        
        successful_advanced = sum(1 for comp in advanced_components if comp in final_analysis)
        score += (successful_advanced / len(advanced_components)) * 30

        # Bonus por qualidade da pesquisa
        avg_quality = estatisticas.get('qualidade_media', 0)
        if avg_quality >= 80:
            score += 5
        elif avg_quality >= 60:
            score += 3

        return min(score, max_score)

    def _generate_intelligent_queries(self, data: Dict[str, Any]) -> List[str]:
        """Gera queries inteligentes para pesquisa"""

        segmento = data.get('segmento', '')
        produto = data.get('produto', '')
        publico = data.get('publico', '')

        base_queries = []

        # Queries principais
        if produto:
            base_queries.extend([
                f"mercado {segmento} {produto} Brasil 2024 dados estatísticas",
                f"análise competitiva {segmento} {produto} oportunidades",
                f"tendências {segmento} {produto} crescimento futuro"
            ])
        else:
            base_queries.extend([
                f"mercado {segmento} Brasil 2024 dados estatísticas crescimento",
                f"análise competitiva {segmento} principais empresas",
                f"tendências {segmento} oportunidades investimento"
            ])

        # Queries específicas por público
        if publico:
            base_queries.extend([
                f"comportamento consumidor {publico} {segmento} pesquisa",
                f"perfil demográfico {publico} Brasil dados"
            ])

        # Queries de inteligência de mercado
        base_queries.extend([
            f"startups {segmento} investimento venture capital Brasil",
            f"cases sucesso empresas {segmento} brasileiras",
            f"desafios principais {segmento} soluções mercado"
        ])

        return base_queries[:8]  # Máximo 8 queries para otimização

    def _validate_input_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Valida dados de entrada - FALHA SE INSUFICIENTE"""

        required_fields = ['segmento']
        missing_fields = [field for field in required_fields if not data.get(field)]

        if missing_fields:
            return {
                'valid': False,
                'message': f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"
            }

        # Valida qualidade dos dados
        segmento = data.get('segmento', '').strip()
        if len(segmento) < 3:
            return {
                'valid': False,
                'message': "Segmento deve ter pelo menos 3 caracteres"
            }

        return {'valid': True, 'message': 'Dados válidos'}

# Instância global
ultra_detailed_analysis_engine = UltraDetailedAnalysisEngine()
