import { Silkscreen } from 'next/font/google'
import { ReactNode } from 'react'

import { cn } from '@/lib/utils'

import SemanaHeader from './header'

interface SemanaLayoutProps {
  children: ReactNode
}

const silkscreen = Silkscreen({
  weight: ['400', '700'], // estilos disponíveis
  subsets: ['latin'], // escolha os subsets necessários
})

export const metadata = {
  title: 'SYMCOMP | Semana da Computação',
  description:
    'A Semana da Computação do IME USP é um dos maiores eventos estudantis de tecnologia e inovação do Brasil. Organizada por alunos do Instituto de Matemática e Estatística da Universidade de São Paulo, reúne palestras, workshops, minicursos e painéis sobre ciência da computação, inteligência artificial, segurança da informação, desenvolvimento de software, design de sistemas e carreira em tecnologia. O evento conecta estudantes, pesquisadores e profissionais da área, promovendo troca de conhecimento, networking e contato direto com as tendências mais atuais do mercado.',
}

export default function SemanaLayout({ children }: SemanaLayoutProps) {
  return (
    <div
      className={cn(
        'h-svh w-full flex flex-col items-center flex-1 bg-[#110F0F] text-white',
        silkscreen.className,
      )}
    >
      <div className="max-w-[1024px] w-full">
        <SemanaHeader />
        {children}
      </div>
    </div>
  )
}
