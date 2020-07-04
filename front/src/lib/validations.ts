export function blankValidation(attr: string): Function {
  return (v: string) => !!v || v.length > 0 || `${attr}を入力してください`;
}

export function maxLengthValidation(attr: string, limit: number): Function {
  return (v: string) => (v && v.length <= limit) || `${attr}は最大${limit}文字以内で入力してください`;
}
