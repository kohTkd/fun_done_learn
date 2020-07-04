const attributes = {
  session: {
    title: 'タイトル'
  }
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function dig(obj: any, keys: string[]): string {
  const key = keys.shift() as string;
  const value = obj[key] || '';
  return typeof value === 'string' ? value : dig(value, keys);
}

export default function attributeNameOf(...keys: string[]): string {
  return dig(attributes, keys);
}
