import { api } from './api'

interface RegisterUser {
  name: string
  email: string
  password: string
}

export default async function RegisterUser({ name, email, password }: RegisterUser) {
  const response = await api.post('/register/', { name, email, password })
  return response
}
