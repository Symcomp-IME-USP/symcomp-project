import { ReactNode } from "react";

interface EnigmaProps {
    children : ReactNode
}

export function EnigmaQA({ children } : EnigmaProps) {

    return (
        <div className="w-full p-5 flex flex-col flex-wrap break-word gap-3">
            <label className="w-full break-words">{children}</label>
            <input className="w-full"></input>
            <button className="w-full">Submit</button>
        </div>
    )
}

export function EnigmaSolved({ children } : EnigmaProps) {
    return (
        <div className="w-full p-5 flex flex-col flex-wrap break-word gap-3">
            <label className="w-full break-words">{children}</label>
            <label className="w-full flex justify-center">Resolvido</label>
        </div>
    )
}