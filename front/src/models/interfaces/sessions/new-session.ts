import ApiParams from '@/models/interfaces/api-params';

export interface NewSession {
  title: string;
}

export interface NewSessionParams extends ApiParams, NewSession {
  title: string;
}
