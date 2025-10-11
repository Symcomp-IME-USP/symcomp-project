import { ReactNode } from 'react'

import { silkscreen } from '@/lib/font'
import { cn } from '@/lib/utils'

import SemanaHeader from './header'

interface SemanaLayoutProps {
  children: ReactNode
}

export const metadata = {
  title: 'SYMCOMP | Semana da Computação',
  description:
    'A Semana da Computação do IME USP é um dos maiores eventos estudantis de tecnologia e inovação do Brasil. Organizada por alunos do Instituto de Matemática e Estatística da Universidade de São Paulo, reúne palestras, workshops, minicursos e painéis sobre ciência da computação, inteligência artificial, segurança da informação, desenvolvimento de software, design de sistemas e carreira em tecnologia. O evento conecta estudantes, pesquisadores e profissionais da área, promovendo troca de conhecimento, networking e contato direto com as tendências mais atuais do mercado.',
}

export default function SemanaLayout({ children }: SemanaLayoutProps) {
  return (
    <div
      className={cn(
        'min-h-svh w-full flex flex-col items-center flex-1 bg-[#110F0F] text-white',
        silkscreen.className,
      )}
    >
      <div className="max-w-[1024px] h-full flex-grow-0 w-full">
        <SemanaHeader />
        {children}
      </div>
    </div>
  )
}
