export interface NewSessionParams {
  title: string;
}

export interface FindSessionParams {
  token: string;
}

export interface ActivityApiInterface {
  token: string;
  title: string;
  created_at?: string | Date;
  updated_at?: string | Date;
}
