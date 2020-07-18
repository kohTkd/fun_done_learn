import Vue from 'vue';
import { Wrapper, createLocalVue, mount } from '@vue/test-utils';
import Vuetify from 'vuetify';
import NewSession from '@/components/index/NewSession.vue';
import SessionForm from '@/models/forms/session-form';

const localVue = createLocalVue();
const context = describe;

describe('NewSession.vue', () => {
  let vuetify: any;
  let wrapper: Wrapper<NewSession>;

  const titleInputItem = () => wrapper.find('input[type="text"][name="title"]');
  const okButton = () => wrapper.find('button');
  const buildForm = ({ title = 'Some Title' }: { title?: string; length?: number } = {}): SessionForm => {
    const form = new SessionForm();
    form.title = length ? title : 'A'.repeat(length);
    return form;
  };

  beforeEach(() => {
    vuetify = new Vuetify();
    wrapper = mount(NewSession, { localVue, vuetify });
  });

  it('has form to create session', () => {
    expect(titleInputItem()).toBeTruthy();
    expect(okButton().text()).toEqual('開始');
    expect(okButton().props().disabled).toBe(false);
  });

  it.skip('emits form when button clicked', async () => {
    titleInputItem().setValue('Some Title');
    await Vue.nextTick();
    expect(okButton().props().disabled).toBe(false);
    okButton().trigger('click');
    const emission = wrapper.emitted('createSession') || [];
    expect(emission.length).toEqual(1);
    const form = buildForm({ title: 'Some Title' });
    expect(emission[1]).toEqual(form);
  });

  context('when input error value', () => {
    it('disables button when blank title', async () => {
      titleInputItem().setValue(undefined);
      await Vue.nextTick();
      expect(okButton().props().disabled).toBe(true);
    });
    it('disables button when too long title', async () => {
      titleInputItem().setValue('A'.repeat(31));
      await Vue.nextTick();
      expect(okButton().props().disabled).toBe(true);
    });
  });

  context('when input threshold', () => {
    it.skip('accepts a character title', async () => {
      titleInputItem().setValue('A');
      await Vue.nextTick();
      expect(okButton().props().disabled).toBe(false);
    });
    it.skip('accepts 30 characters title', async () => {
      titleInputItem().setValue('A'.repeat(30));
      await Vue.nextTick();
      expect(okButton().props().disabled).toBe(false);
    });
  });
});
