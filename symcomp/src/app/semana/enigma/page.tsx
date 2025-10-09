import { EnigmaQA, EnigmaSolved } from "@/components/enigma/enigmaQA"

interface QAProps {
    question : string,
    solved : boolean
}

const QA : QAProps[] = [
    {
        question : "Digite os 5 primeiros dígitos do PI",
        solved : false
    },
    {
        question :"Quantos anos tem o BCC?",
        solved : false
    },
    {
        question : "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        solved : true
    }
]

export default function EnigmaPage() {
    return (
        <main>
            <div className="flex justify-center">
                <h2>Enigmas da 15 Semana da Computação</h2>
            </div>
            <form className="m-5">
                {
                    QA.map(q => (
                        q.solved == false
                            ? <EnigmaQA children={q.question}></EnigmaQA> 
                            : <EnigmaSolved children={q.question}></EnigmaSolved>
                    ))
                }
            </form>
        </main>
    )
}