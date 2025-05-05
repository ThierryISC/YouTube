from typing import TypedDict
import requests
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph

API_KEY = "pub_84311f56b9eaf200813dbcd02ae71af7707ea"

class AgentState(TypedDict):
    sujet : str
    infos : str
    resume : str

llm = OllamaLLM(model="llama3")

def recherche_infos(state):
    print('Recherche des infos...')
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": API_KEY,
        "q" : state["sujet"],
        "language": "fr",
        "country": "fr"
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        print('Erreur API !!')
        exit(0)
    articles = r.json().get("results", [])
    titres = "\n ".join(" - " + article['title'] for article in articles)
    return {"suject": state["sujet"], "infos": titres, "resume": ""}


def resume_infos(state):
    print('Résumé des infos...')
    prompt = f"Rédige en français un article de presse de 4 lignes maxi, sans bullet point, qui résume les informations suivantes : {state['infos']}"
    reponse = llm.invoke(prompt)
    return {"suject": state["sujet"], "infos": state["infos"], "resume": reponse}



workflow = StateGraph(state_schema=AgentState)
workflow.add_node("rechercher", recherche_infos)
workflow.add_node("resumer", resume_infos)

workflow.set_entry_point("rechercher")
workflow.add_edge("rechercher", "resumer")
workflow.set_finish_point("resumer")

graph = workflow.compile()

sujet = input("Sur quel sujet dois-je faire les recherches ? ")
resultat = graph.invoke({"sujet": sujet})
print('Voici le résumé sur ', sujet)
print(resultat["resume"])