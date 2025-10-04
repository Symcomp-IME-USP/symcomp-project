// Nessa página o usuário verifica seu email com o código enviado.

'use client'

import { zodResolver } from '@hookform/resolvers/zod'
import { useMutation } from '@tanstack/react-query'
import Image from 'next/image'
import { useForm } from 'react-hook-form'
import z from 'zod'

import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import VerifyCode from '@/lib/http/verify-code'

const verificationSchema = z.object({
  email: z.email(),
  code: z.string(),
})

const email = localStorage.getItem('email') || ''

export default function VerificarPage() {
  const form = useForm<z.infer<typeof verificationSchema>>({
    resolver: zodResolver(verificationSchema),
    defaultValues: {
      email,
      code: '',
    },
  })

  const { isPending, mutate } = useMutation({
    mutationFn: async (values: z.infer<typeof verificationSchema>) => {
      return await VerifyCode(values)
    },
    onSuccess: (data) => {
      console.log('Verificação realizada com sucesso:', data)
    },
    onError: (error) => {
      console.error('Erro na verificação:', error)
    },
  })

  function onSubmit(values: z.infer<typeof verificationSchema>) {
    mutate(values)
  }

  return (
    <div className="max-w-2xl mx-auto p-6 grid gap-6">
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="border rounded-2xl p-6 shadow-sm bg-white grid gap-4"
        >
          <Image
            alt="Logo da Symcomp"
            src="/logo/symcomp.png"
            width={80}
            height={80}
            className="mx-auto"
          />

          <h2 className="text-xl font-semibold">Verificar email</h2>

          <p className="text-sm">
            Um código de verificação foi enviado para o email{' '}
            <span className="font-mono bg-rose-200 p-1">{form.getValues().email}</span>.
            Insira o código abaixo para finalizar o cadastro.
          </p>

          <FormField
            control={form.control}
            name="code"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Código</FormLabel>
                <FormControl>
                  <Input {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <button
            type="submit"
            disabled={isPending}
            className={`bg-rose-600 text-white rounded px-4 py-2 mt-2 ${isPending ? 'hover:bg-rose-700' : 'opacity-80'}`}
          >
            Verificar
          </button>
        </form>
      </Form>
    </div>
  )
}
