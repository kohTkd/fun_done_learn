import { PlacementApiInterface } from './placements';

export interface NewActivityParams {
  session_token: string;
  content: string;
}

export interface UpdateActivityParams extends NewActivityParams {
  token: string;
}

export interface ActivityApiInterface {
  session_token: string;
  token: string;
  content: string;
  created_at?: string | Date;
  updated_at?: string | Date;
  placement?: PlacementApiInterface;
}
