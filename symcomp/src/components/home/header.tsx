import { MenuIcon, MenuSquareIcon } from 'lucide-react'
import Image from 'next/image'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '../ui/dropdown-menu'
import { Navigation } from '../ui/navigation'

export const HomeHeader = () => {
  const estilo_nav_item = 'hover:bg-primary'
  const sections = [
    {
      label: 'Início',
      href: 'home',
    },
    {
      label: 'Projetos',
      href: 'projects',
    },
    {
      label: 'Quem somos',
      href: 'about',
    },
  ]

  return (
    <div className="flex flex-row h-[100px] px-6 gap-2 items-center justify-between w-full bg-background">
      <a href="#home">
        <Image
          alt="Logo da Symcomp"
          src="/logo/symcomp.png"
          width={100}
          height={100}
          className="flex size-[60px]"
        />
      </a>
      <DropdownMenu>
        <DropdownMenuTrigger className="sm:hidden">
          <MenuIcon size={32} color="white" />
        </DropdownMenuTrigger>
        <DropdownMenuContent className="mr-6 p-8">
          <Navigation navItem={sections} classNavItem={estilo_nav_item} />
        </DropdownMenuContent>
      </DropdownMenu>
      <Navigation
        className="hidden sm:flex"
        navItem={sections}
        classNavItem={estilo_nav_item}
      />
    </div>
  )
}
